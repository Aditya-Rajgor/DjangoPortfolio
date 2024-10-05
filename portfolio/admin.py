from django.contrib import admin
from .models import Project, IPDatabase, Traffic
from .forms import Contact
from django.shortcuts import render
import folium
from django.utils import timezone
from datetime import timedelta


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'status')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'timestamp', 'email', 'subject', 'message')

@admin.register(IPDatabase)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'timestamp', 'latitude', 'longitude', 'city', 'org')

@admin.register(Traffic)
class TrafficAdminView(admin.ModelAdmin):
    change_list_template = "admin/traffic.html"

    def changelist_view(self, request, extra_context=None):
        # Optionally pass additional context here
            # Create a base map
        m = folium.Map(location=[0, 0], zoom_start=2, tiles='CartoDB dark_matter')  # Center at [0, 0] and zoom out to see most of the world

        # Get current time
        now = timezone.now()

        # Define time ranges
        one_day_ago = now - timedelta(days=1)
        one_week_ago = now - timedelta(days=7)

        # Fetch all unique IP addresses with location data from the database
        ip_addresses = IPDatabase.objects.exclude(latitude__isnull=True, longitude__isnull=True)

        # Calculate the total number of IP addresses
        total_ips = ip_addresses.count()

        # Add markers to the map for each IP address
        for ip_entry in ip_addresses:

            try:
                latitude = float(ip_entry.latitude)
                longitude = float(ip_entry.longitude)
                city = ip_entry.city if ip_entry.city else "Unknown location"
                timestamp = ip_entry.timestamp
                print(f"Processing IP Entry: {ip_entry.ip_address}, City: {city}, Timestamp: {timestamp}")
                
                # Ensure timestamp is not None
                if timestamp is not None:
                    # Format timestamp
                    formatted_timestamp = timestamp.strftime("%d %b, %y <br> %I:%M %p")

                    # Determine marker color based on timestamp
                    if timestamp >= one_day_ago:
                        marker_color = 'red'  # Within 1 day
                    elif timestamp >= one_week_ago:
                        marker_color = 'lightblue'  # Within 1 week
                    else:
                        marker_color = 'gray'  # Older than 1 week
                else:
                    # Default color if timestamp is None
                    marker_color = 'green'
                    formatted_timestamp = "Unknown"

                
                # Add marker to the map with a Tooltip for hover effect
                folium.Marker(
                    location=[latitude, longitude],
                    tooltip=folium.Tooltip(f"<b>IP:</b> {ip_entry.ip_address}<br>City: {city}<br>Time: {formatted_timestamp}"),
                    icon=folium.Icon(color=marker_color, icon='info-sign')
                ).add_to(m) 
            
            except (ValueError, TypeError):
                
                # Skip any entries with invalid data
                continue

        # Convert the map to HTML representation
        map_html = m._repr_html_()
        context = {
          'map': map_html, 
          'total_ips': total_ips
        }
        return super().changelist_view(request, extra_context=context)

import sys
from unittest import loader
from django.shortcuts import render
from django.template import Context
from .models import Project, Skill, IPDatabase
from .forms import ContactForm
from django.core.mail import send_mail
import folium
import requests
from datetime import timedelta
from django.utils import timezone
from django.http import HttpResponseForbidden, HttpResponseServerError
import os

def custom_500(request):
    return render(request, "500.html", status=500)


def home(request):

    # Get the client's IP address
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')


    # Check if the IP is already in the database
    if not IPDatabase.objects.filter(ip_address=ip).exists():
        # Fetch location data using an IP geolocation API
        try:
            # Replace 'YOUR_API_KEY' with your actual API key
            response = requests.get(f"https://ipinfo.io/{ip}?token={os.getenv('IP_TOKAN_KEY')}")
            data = response.json()

            # Extract latitude, longitude, and city information
            location = data.get('loc', '')  # 'loc' is usually in 'latitude,longitude' format
            latitude, longitude = location.split(',') if location else ('', '')
            city = data.get('city', '')

            # Save the IP and location data to the database
            IPDatabase.objects.create(
                ip_address=ip,
                latitude=latitude,
                longitude=longitude,
                city=city
            )
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
           
            # Send an email
            subject = form.cleaned_data['subject']
            message = "Name--->" + form.cleaned_data['name'] + "   \nfrom --->" + form.cleaned_data['email'] + "    \n" + "message--->" + form.cleaned_data['message']
            from_email = form.cleaned_data['email']
            recipient_list = ['adityarajgor88@gmail.com']  # Replace with your email address

            send_mail(
                subject,
                message,
                from_email,
                recipient_list,
                fail_silently=False,
            )

            #form = ContactForm()  # Clear the form after saving


    else:
        form = ContactForm()

    projects = Project.objects.all().order_by('-created_date')
    skills = Skill.objects.all()
        
    context = {
        'form': form,
        'projects': projects, 'skills': skills
        # Add other context variables here if needed
    }
        
    return render(request, 'portfolio/home.html', context)


def admin_traffic_view(request):

    # Check if the user is an admin
    if not request.user.is_superuser:
        return HttpResponseForbidden("You are not authorized to view this page.")

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
            org = ip_entry.org
            timestamp = ip_entry.timestamp
            #print(f"Processing IP Entry: {ip_entry.ip_address}, City: {city}, Timestamp: {timestamp}")
            
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
                tooltip=folium.Tooltip(f"<b>IP:</b> {ip_entry.ip_address}<br>City: {city}<br>Time: {formatted_timestamp}<br>Org: {org}"),
                icon=folium.Icon(color=marker_color, icon='info-sign')
            ).add_to(m) 
           
        except (ValueError, TypeError):
            
            # Skip any entries with invalid data
            continue

    # Convert the map to HTML representation
    map_html = m._repr_html_()

    return render(request, 'admin/traffic.html', {'map': map_html, 'total_ips': total_ips})
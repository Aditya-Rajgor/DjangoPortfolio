from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateField()
    status = models.CharField(max_length=100)
    github = models.CharField(max_length=300, blank=True, null=True)
    linkedin = models.CharField(max_length=300, blank=True, null=True)
    photo = models.CharField(max_length=500)

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"Message from {self.name}"
    
class IPDatabase(models.Model):
    ip_address = models.CharField(max_length=45, unique=True)  # Supports both IPv4 and IPv6
    timestamp = models.DateTimeField(auto_now_add=True)  # Time of the first visit
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    org = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.ip_address
    
class Traffic(models.Model):
    name = models.CharField(max_length=20, unique=True)
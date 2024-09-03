from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateField()
    status = models.CharField(max_length=100)
    github = models.CharField(max_length=300)
    linkedin = models.CharField(max_length=300)
    photo = models.CharField(max_length=500)

    def __str__(self):
        return self.title
    

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('Programming Languages', 'Programming Languages'),
        ('Tools', 'Tools'),
        ('Soft Skills', 'Soft Skills'),
    ]


    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

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
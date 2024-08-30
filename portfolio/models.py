from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateField()
    status = models.CharField(max_length=100)
    github = models.CharField(max_length=300)

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
    
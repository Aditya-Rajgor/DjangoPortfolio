from django.shortcuts import render
from .models import Project, Skill
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
           
            # Send an email
            subject = form.cleaned_data['subject']
            message = "message--->" + form.cleaned_data['message'] + "   \nfrom --->" + form.cleaned_data['email']
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

    projects = Project.objects.all()
    skills = Skill.objects.all()
        
    context = {
        'form': form,
        'projects': projects, 'skills': skills
        # Add other context variables here if needed
    }
        
    return render(request, 'portfolio/home.html', context)

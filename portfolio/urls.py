from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('linkedin-privacy-policy', views.linkedin_pp, name='linkedin_pp')
]

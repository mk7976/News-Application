from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="home"),
    path("bussiness/", views.businessPage, name="business"),
    path("health/", views.HealthPage, name="health"),
    path("sports/", views.SportsPage, name="sports"),
    path("technology/", views.TechnologyPage, name="technology"),
    path("politics/", views.PoliticalPage, name="politics"),
    path("about/", views.About, name="about"),
    path("contact/", views.Contact, name="contact"),
    path("sendmassage/", views.SendMassage, name="sendmessage"),
#admin
    #1234
]

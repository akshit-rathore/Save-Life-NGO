from django.urls import path
from . import views

urlpatterns = [
    path('', views.events, name="events"),
    path('<int:id>', views.single_event, name="single"),
]
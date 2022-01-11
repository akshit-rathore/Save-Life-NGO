from django.urls import path
from . import views

urlpatterns = [
    path('', views.Donation, name="donation"),
    path('pay', views.bill, name="bill"),
    path('success', views.success, name="success"),
    path('fail', views.fail, name="fail"),
]
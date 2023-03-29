from django.urls import path, include
from .api.ClientMasterApi import ClientMasterApi



urlpatterns = [
    path('check_url',ClientMasterApi.as_view()),
   
]
from django.urls import path, include
from .api.CheckwhitelistedApi import check_whitelisted_url



urlpatterns = [
    path('check_url',check_whitelisted_url.as_view()),
   
]
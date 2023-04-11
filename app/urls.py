from django.urls import path, include
from .api.ClientMasterApi import UserAuthAPI


urlpatterns = [
    path('check_url',UserAuthAPI.as_view()),
   
]
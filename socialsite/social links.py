from django.contrib import admin
from django.urls import path
from social import views as soc_views
url_pattern=[
    path("social/login",soc_views.login.get_to_login,"login")
    
]
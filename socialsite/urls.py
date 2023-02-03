"""socialsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from socialsite import sociallinks as soc_link
from social import views as soc_views
from django.conf import settings
from django.conf.urls.static import static
from personality import views as person_view
urlpatterns = [
    path("admin/", admin.site.urls),
    path("social/login",soc_views.login.get_to_login,name="login"),
    path("social/rigster",soc_views.login.register,name='register'),
    path("social/user/account",soc_views.login.login_op,name="account"),
    path("social/user/interest",person_view.settings.get_to_basic_info,name='interests'),
    path("ajax/ad/fav",person_view.settings.add_fav,name='add_fav'),
    path("ajax/del/fav",person_view.settings.delete_fav,name='del_fav')
    ]
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_URL)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

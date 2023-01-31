from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from social.models import *
from django.shortcuts import render
import hashlib
import os

# Create your views here.
class login:
    def get_countries():
        all_countries=[]
        for city in list(cities.objects.all()):
            country=allowed_countrys.objects.filter(id=city.country_id_id)
            all_countries.append({"country":list(country.all())[0].country_name,"city":{"id":city.id,"name":city.city_name}})
        return all_countries
    def get_to_login(request):
        template=loader.get_template("landing.html")
        all_countries=login.get_countries()
        return render(request,"landing.html",{"countries":all_countries})
    def register(request):
        if request.POST.get("password")==request.POST.get("confirm_passwords"):
            USER=user()
            USER.user_name=request.POST.get("first_name")+request.POST.get("famile_name")
            USER.user_email=request.POST.get("email")
            USER.user_phone=request.POST.get("phone")
            USER.user_country=request.POST.get("city")
            salt = os.urandom(16)
            hash = hashlib.md5()
            hash.update(request.POST.get("password").encode("utf-8"))
            USER.user_password=hash.hexdigest()
            USER.save()
            return render(request,"landing.html",{"result":"تمت عملية التسجيل","countries":login.get_countries()})
        else:
            return render(request,"landing.html",{"result":"لم تتم عملية التسجيل بنجاح","countries":login.get_countries()})
    def login_op(request):
        if request.method=="POST":
            hash = hashlib.md5()
            hash.update(request.POST.get("password").encode("utf-8"))
            password=user.objects.filter(user_name=request.POST.get("user_name"),user_password=hash.hexdigest()).get().user_password
            print(type(password))
            print(hash.hexdigest()==password)
            print(user.objects.filter(user_name=request.POST.get("user_name")).get().user_profile_img)
            request.session["user_id"]=user.objects.filter(user_name=request.POST.get("user_name")).get().id
            if password==hash.hexdigest():
                return render(request,"about.html",{"account":user.objects.filter(user_name=request.POST.get("user_name")).get()})
            return render(request,"landing.html",{"result":"خطأ فى البيانات","countries":login.get_countries()})
    
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from social.models import *
from django.shortcuts import render
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
            USER.save()
            return render(request,"landing.html",{"result":"تمت عملية التسجيل","countries":login.get_countries()})
        else:
            return render(request,"landing.html",{"result":"لم تتم عملية التسجيل بنجاح","countries":login.get_countries()})
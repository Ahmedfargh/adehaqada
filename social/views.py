from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.
class login:
    def get_to_login(request):
        template=loader.get_template("landing.html")
        return HttpResponse(template.render({},request))
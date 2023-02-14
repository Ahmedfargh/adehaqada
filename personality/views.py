from django.shortcuts import render
from social.models import user
from django.shortcuts import render
from .models import personalfavoirte,favorite,work_education
from django.http import HttpResponse
from django.http import JsonResponse
from social.views import login
# Create your views here.
class settings:
    def get_all_interests(user_id):
        all_interests=[]
        user_object=user.objects.filter(pk=user_id)
        for fav in list(personalfavoirte.objects.filter(personal_name_id=user_id)):
            favorite_name=favorite.objects.filter(pk=fav.favorite_value_id)
            all_interests.append(favorite_name.get().favorite)
        print(all_interests)
        return all_interests
    def get_to_basic_info(request):
        user_id=request.session["user_id"]
        user_data=user.objects.filter(id=user_id)
        #interests=personalfavoirte.objects.filter(personal_name_id=user_id)
        interests=settings.get_all_interests(user_id)
        return render(request,"edit-interest.html",{"user_data":user_data.get(),"interests":interests,"all_interests":favorite.objects.all()})
    def add_fav(request):
        try:
            if len(personalfavoirte.objects.filter(pk=request.POST.get("fav_name"),personal_name_id=request.session["user_id"])):
                return JsonResponse({"result":"بنجاح"+request.POST.get("fav_name")+"تم أضافة "})
            print(request.POST.get("fav_name"))
            fav_id=favorite.objects.filter(pk=request.POST.get("fav_name"))
            personal_fav=personalfavoirte()
            personal_fav.personal_name_id=request.session["user_id"]
            personal_fav.favorite_value=fav_id.get()
            personal_fav.save()
            print("good")
            return JsonResponse({"result":"بنجاح"+request.POST.get("fav_name")+"تم أضافة "})
        except  Exception:
            raise
    def delete_fav(request):
        try:
            if len(personalfavoirte.objects.filter(pk=request.POST.get("personal_fav_id"),personal_name_id=request.session["user_id"])):
                return JsonResponse({"result":"بنجاح"+request.POST.get("fav_name")+"تم أضافة "})
            personalfavoirte.objects.filter(favorite_value_id=request.POST.get("personal_fav_id"),personal_name_id=request.session["user_id"]).delete()
            return JsonResponse({"result":"بنجاح"+request.POST.get("personal_fav_id")+"تم أضافة "})
        except:
            raise
    def get_To_work_and_education(request):
        user_id=request.session["user_id"]
        user_data=user.objects.filter(id=user_id)
        return render(request,"edit-work-eductation.html",{"countries":login.get_countries(),"user_data":user_data.get()})
    def add_work_and_education(request):
        try:
            work=request.POST.get("job")
            worker=request.session["user_id"]
            start_date=request.POST.get("start_date")
            end_date=request.POST.get("end_date")
            country=request.POST.get("country")
            work_obj=work_education()
            work_obj.work_name=work
            work_obj.from_date=start_date
            work_obj.to_date=end_date
            work_obj.worker=user.objects.filter(pk=worker).get()
            work_obj.city=country
            work_obj.save()
            return JsonResponse({"result":"تمت العملية بنجاح"})
        except:
            raise

from django.db import models
from datetime import datetime
# Create your models here.
class allowed_countrys(models.Model):
    country_name=models.TextField(max_length=25)
class cities(models.Model):
    city_name=models.CharField(max_length=40)
    country_id=models.ForeignKey(allowed_countrys,on_delete=models.CASCADE)
class user(models.Model):#this model is to access users data
    user_name=models.CharField(max_length=45)
    user_email=models.EmailField(max_length=31,null=True)
    user_phone=models.CharField(max_length=30)
    user_profile_img=models.FileField(default="/media/img/users/find_user.png")
    user_country=models.CharField(max_length=40)
    user_password=models.CharField(max_length=120,null=True)
    user_online=models.BooleanField(default=False)
    user_background=models.ImageField(upload_to="img/users/",default="img/users/assassins_creed-wallpaper-1920x1200.jpg")
    def convert_to_dict(self):
        return {
            "user_name":self.user_name,
            "user_email":self.user_email,
            "user_phone":self.user_phone,
            "user_country":self.user_country,
            "user_password":self.user_password,
            "user_profile_img":self.user_profile_img
        }
class media(models.Model):#any media video,images
    media_link=models.CharField(max_length=100)
    owned_by=models.ForeignKey(user,on_delete=models.CASCADE)
    uploaded_at=models.DateTimeField(default=datetime.now())
    media_id=models.BigIntegerField()
class post(models.Model):#acess posts
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    post_content=models.CharField(max_length=10000)
    post_id=models.BigIntegerField()
    uploaded_at=models.DateTimeField(default=datetime.now())
class reaction(models.Model):#any reaction you do
    reaction_type=models.CharField(max_length=100)
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    post_id=models.ForeignKey(post,on_delete=models.CASCADE)
class friend_ships(models.Model):#the relation amoung peoples
    user_1=models.BigIntegerField()
    user_2=models.BigIntegerField()
    friend_type=models.IntegerField()

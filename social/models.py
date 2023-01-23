from django.db import models
from datetime import datetime
# Create your models here.
class allowed_countrys(models.Model):
    country_name=models.TextField(max_length=25)
    country_id=models.BigIntegerField()
class cities(models.Model):
    city_name=models.CharField(max_length=40)
    city_id=models.BigIntegerField()
    country_id=models.ForeignKey(allowed_countrys,on_delete=models.CASCADE)
class user(models.Model):#this model is to access users data
    user_name=models.CharField(max_length=45)
    user_email=models.EmailField(max_length=31,null=True)
    user_phone=models.CharField(max_length=30)
    user_id=models.BigIntegerField()
    user_profile_img=models.FileField(default="/media/img/users/find_user.png")
    user_country=models.ForeignKey(cities,on_delete=models.CASCADE)
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

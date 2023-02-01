from django.db import models
from social.models import *
from datetime import datetime
# Create your models here.
class favorite(models.Model):
    favorite=models.CharField(max_length=50)
class personalfavoirte(models.Model):
    personal_name=models.ForeignKey(user,on_delete=models.CASCADE)
    favorite_value=models.ForeignKey(favorite,on_delete=models.CASCADE)
class personal_dates(models.Model):
    date=models.DateField(null=False)
    person=models.ForeignKey(user,on_delete=models.CASCADE)
class work_education(models.Model):
    work_name=models.CharField(max_length=50)
    worker=models.ForeignKey(user,on_delete=models.CASCADE)
    from_date=models.DateField(null=True)
    to_date=models.DateField(default=datetime.now())
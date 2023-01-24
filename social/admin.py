from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(user)
admin.site.register(media)
admin.site.register(post)
admin.site.register(reaction)
admin.site.register(friend_ships)
admin.site.register(allowed_countrys)
admin.site.register(cities)
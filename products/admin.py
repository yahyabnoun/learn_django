from django.contrib import admin
from .models import Product, User, Video

# Register your models here.
admin.site.register(Product)
admin.site.register(Video)
admin.site.register(User)
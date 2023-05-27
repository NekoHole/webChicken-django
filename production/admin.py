from django.contrib import admin
from .models import Category, Tag, Type, Product, Image
# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Type)
admin.site.register(Product)
admin.site.register(Image)
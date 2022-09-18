from django.contrib import admin
from .models import Category, Medicine, Brand
# Register your models here.
admin.site.register(Medicine)
admin.site.register(Brand)
admin.site.register(Category)
from tkinter import Image
from django.contrib import admin
from .models import Category, Inventory, Medicine, Brand, Image
# Register your models here.
admin.site.register(Medicine)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Inventory)
admin.site.register(Image)

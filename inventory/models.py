from tabnanny import verbose
from django.db import models

# Create your models here.
class Brand(models.Model):
    brand_id = models.BigAutoField(primary_key=True,null=False,default=0)
    brand_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return super().__str__(self.brand_name)
    
class Category(models.Model):
    category_name = models.CharField(max_length=270)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self) -> str:
        return super().__str__(self.category_name)

class Medicine(models.Model):
    medicine_name = models.CharField(max_length=270)
    quantity = models.IntegerField()
    price = models.FloatField()
    is_active = models.BooleanField(default=True)
    storage_date = models.DateField(auto_now=True)


    class Meta:
        ordering = ['storage_date']
    def __str__(self) -> str:
        return super().__str__(self.medicine_name)




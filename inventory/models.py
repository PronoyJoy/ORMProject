
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
    slug = models.SlugField(null=True)
    is_active = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self) -> str:
        return super().__str__(self.category_name)


#product
class Medicine(models.Model):
    medicine_name = models.CharField(max_length=270)
    description = models.CharField(max_length=300,null=True)
    slug = models.SlugField(null=True)
    med_category_name = models.ManyToManyField(Category,null=True)
    med_brand_name = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
   
    
    

    
    def __str__(self) -> str:
        return super().__str__(self.medicine_name)



class Inventory(models.Model):
    inventory_id = models.CharField(max_length=10,unique=True,primary_key=True)
    product_name = models.ForeignKey(Medicine,on_delete=models.CASCADE)
    inventory_price = models.DecimalField(max_digits=7,decimal_places=3)
    unit_price = models.DecimalField(max_digits= 5,decimal_places=2)
    is_active = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True, editable = False)
    quantity = models.IntegerField()
    promotion_price = models.DecimalField(max_digits=5,decimal_places=2)
    promotion_is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Inventory'

    def __str__(self) -> str:
        return super().__str__(self.product_name)

class Image(models.Model):
    url = models.FileField(upload_to=None)
    alternative_text = models.CharField(max_length=100)
    inventory = models.ForeignKey(Inventory,on_delete=models.CASCADE)
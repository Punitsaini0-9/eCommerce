from django.db import models

# Create your models here.

# class Category(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.CharField(max_length=300)

#     def __str__(self):
#         return self.name

# class Tags(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.CharField(max_length=300)

#     def __str__(self):
#         return self.name
    
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=100 , default = "")
    # tags = models.ManyToManyField(Tags)
    sub_category = models.CharField(max_length = 50 , default = "")
    price = models.IntegerField(default = 0)
    description = models.CharField(max_length=300)
    publish_date = models.DateField()
    image = models.ImageField(upload_to ='shop/images' , default = "")

    def __str__(self):
        return self.product_name
    
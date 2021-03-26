from django.db import models

# Create your models here.
class product(models.Model):
    product_id = models.AutoField
    product_name=models.CharField(default='lorem ipsum', max_length=50)
    image= models.ImageField(upload_to="shop/images",default="")
    price = models.IntegerField(default=0)
    product_desc=models.CharField(default=' ', max_length=300)
    customer_review=models.CharField(default=' ', max_length=300)

    def __str__(self):
        return self.product_name


    

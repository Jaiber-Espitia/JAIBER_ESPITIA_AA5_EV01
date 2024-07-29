from django.db import models

# Create your models here.
class Products(models.Model):
    PRODUCT_BRAND = (

        ("AP", "Apple"),
        ("MC", "Microsoft"),
        ("NV", "Nvidia"),
        ("RZ", "Ryzen"),
        ("IN", "Intel")
        
        )

    name = models.CharField(
        max_length=30,
        null=False, 
        verbose_name="product name"
    )
    
    brand = models.CharField(
        max_length=10,
        choices=PRODUCT_BRAND
        )
    
    description = models.TextField(
        max_length=500
        )
    
    price = models.FloatField(
        null=False
        )
    
    quantity = models.IntegerField(null=False)

    
    class Meta:
        verbose_name = "Products"
        ordering = ["name"]
        verbose_name_plural = "My products"

    
    def __str__(self):
        return "{}, {}".format(self.name, self.price)
    

from django.db import models
from django.urls import reverse

from shop.settings import AUTH_USER_MODEL 
# Create your models here.


class Product(models.Model):

    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="product",blank=True,null=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("product_detail",kwargs={"slug":self.slug})
    

# raticle(order)    
"""
-utilisateur
-Produit
-quanitte
commande ou non
"""

class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})" 


#panier(cart)

"""
uilisateur
Articles
commande ou non

date de la commende

"""

class cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL,on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True,null=True)
    # blank=True permet despecifier une valeur null a un champ qui n'est pas de type text


    def __str__(self) :
        return self.user.username
     
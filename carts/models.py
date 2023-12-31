from django.db import models
from store.models import Product, Variation
from django.contrib.auth.models import User
from accounts.models import Account

# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    # class Meta:
    #     db_table = 'Cart'
    #     ordering = ['date_added']

    def __str__(self):
        return self.cart_id
    
class CartItem(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True) # on_delete=models.CASCADE means that if the user is deleted, the cart item will also be deleted. It is a good practice to delete the cart item when the user is deleted. It is a good practice
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation, blank=True) # blank=True means that the field is optional. It is not required to add variations to the cart item. It is optional because it is not required to add variations to the cart item. It is optional because it is not required to add
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.product
    
    def sub_total(self):
        return self.product.price * self.quantity
    
    # class Meta:
    #     db_table = 'CartItem'
    #     ordering = ['product']
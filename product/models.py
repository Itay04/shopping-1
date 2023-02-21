from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    image = models.ImageField(null=True, blank=True,
                              default='/placeholder.png')
    def _str_(self):
        return self.name

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.product.name - self.quantity

    def get_total(self):
        return self.product.price * self.quantity

# class order(models.Model):
#     DataField
#     OrderID

# class OrderItem(models.Model):
# #     UserId = 
# #     OrderID = 
# #     product = models.ForeignKey(Product)
# #     quantity = models.IntegerField()
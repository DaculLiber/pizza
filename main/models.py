from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Pizzas(models.Model):
    # DB model to keep info about pizza 
    
    name = models.CharField(max_length=200) 
    description = models.TextField() # Ingredients n stuff
    photo = models.ImageField(upload_to='main/img', default='main/img/pizza.jpg')
    price = models.IntegerField(default=15)
    
    class Meta:
        verbose_name_plural = "Pizzas"

    def __str__(self):
        return self.name



class Orders(models.Model):
    # Orders table

    user = models.ForeignKey(User, on_delete=models.CASCADE) # who has ordered the pizza/pizzas
    price = models.IntegerField(default=0) # Price of the orde (make a function or something to calculate this)
    address = models.CharField(max_length=300) # User gives it
    content = models.ManyToManyField(Pizzas) # Self explainatory
    date = models.DateTimeField("Date Ordered", default=timezone.now())

    class Meta:
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"{self.user} - {self.price}"



# Create your models here.

class Toppings(models.Model):
    # Toppings
    
    topping = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Toppings"

    def __str__(self):
        return f"{self.topping}: {self.price}"

# class Prices(models.Model):
#     # Model to link pizza to size and price, aka a pizza can have multiple sizes and every size has a price

#     SIZES = [
#         ("XL", "Extra-Large"),
#         ("L", "Large"),
#         ("M", "Medium"),
#         ("S", "Small"),
#     ]

#     price = models.IntegerField(default=0) 
#     size = models.CharField(max_length=2, choices=SIZES)
#     pizza = models.ForeignKey(Pizzas, on_delete=models.CASCADE)
#     extras = models.ManyToManyField(Toppings, blank=True, related_name="extras")

#     class Meta:
#         verbose_name_plural = "Prices"

#     def __str__(self):
#         return f"{self.pizza} {self.size}: {self.price}"

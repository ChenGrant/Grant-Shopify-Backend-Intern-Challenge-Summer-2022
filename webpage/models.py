from django.db import models


# Create your models here.
class Product(models.Model):
    description = models.CharField(max_length = 100, default = "")
    price = models.DecimalField(max_digits = 9, decimal_places = 2, validators=[MinValueValidator(0)])
    quantity = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.description

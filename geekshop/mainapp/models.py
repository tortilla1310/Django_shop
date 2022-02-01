from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name="name", max_length=100)
    description = models.TextField(verbose_name="description", blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="name", max_length=100)
    price = models.DecimalField(
        verbose_name="price", max_digits=7, decimal_places=2, default=0
    )
    color = models.PositiveIntegerField(verbose_name="color", default=0x000000)
    description = models.TextField(verbose_name="description", blank=True)
    image = models.ImageField(verbose_name="image", blank=True, upload_to="products")
    quantity = models.PositiveIntegerField(verbose_name="quantity", default=0)

    def __str__(self):
        return self.name

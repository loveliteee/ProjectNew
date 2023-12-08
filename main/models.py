from django.db import models
from users.models import User

class ProductCategory(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField( unique=True, max_length=128)

    description = models.TextField()

    def __str__(self):
        return self.name

class Feature(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название характеристики')
    
    value = models.CharField(max_length=255, verbose_name='Значение характеристики')

    def __str__(self):
        return f'{self.name}: {self.value}'

class Product(models.Model):
   id = models.AutoField(primary_key=True)

   name = models.CharField("Наименование товара", max_length=255)

   description = models.TextField("Описание")

   price = models.FloatField("Цена")

   quantity = models.IntegerField("Количество")

   image = models.ImageField("Изображение", upload_to='products')

   category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True)

   features = models.ManyToManyField(Feature, blank=True, related_name='products', verbose_name='Характеристики')

   def __str__(self):
       return f'Продукт: {self.name} | Категория: {self.category.name}'


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)



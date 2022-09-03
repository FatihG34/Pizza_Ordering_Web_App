from django.db import models

# Create your models here.
class Size(models.Model):
    SIZE = [
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    ]
    title = models.CharField('Size', max_length=10, choices=SIZE)

    def __str__(self):
        return self.title

class Pizza(models.Model):
    topping1 = models.CharField('Topping_1', max_length=30)
    topping2 = models.CharField('Topping_2', max_length=30)
    size = models.ForeignKey(Size,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.size} Pizza with {self.topping1} and {self.topping2} '

class Quant(models.Model):
    quant =[
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
        ('6', 6),
    ]
    number = models.CharField('Number', max_length=2, choices=quant)
from django.db import models
from orders import choices

"""После слияния это надо убрать"""


class Product(models.Model):
    name = models.CharField()


"""После слияния проекта надо в отдельный файл пихать"""


class User(models.Model):
    name = models.CharField()


"""Тут уже под себя сделаешь как нибудь"""


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    sum = models.IntegerField()
    address = models.CharField()
    date = models.DateField(auto_now_add=True)
    status = models.CharField(choices=choices, default='В обработке', verbose_name="Статус")


class OrderProduct(models.Model):
    pass


class OrderInfo(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

from django.db import models


class Menu(models.Model):
    title = models.CharField('Назва страви', max_length=50)
    price = models.CharField('Ціна', max_length=10)
    components = models.TextField('Компоненти страви')
    category = models.CharField('Категорія', max_length=15)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class Reservation(models.Model):
    name = models.CharField('Ім`я', max_length=90)
    seat = models.CharField('Місце', max_length= 2)
    phone_number = models.CharField('Номер телефону', max_length=15)
    quantity_of_people = models.IntegerField('Кількість людей')
    date = models.DateField('Дата')
    time = models.TimeField('Час')
    note = models.TextField('Примітка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бронювання'
        verbose_name_plural = 'Бронювання'


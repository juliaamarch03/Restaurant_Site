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

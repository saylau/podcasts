from django.db import models

# Create your models here.

class City(models.Model):
    city_kz = models.CharField(max_length=250)
    city_ru = models.CharField(max_length=250)
    
    def __str__(self):
        return self.city_ru

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

class Contact(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='contacts', verbose_name='Город')
    phone_number = models.CharField(max_length=12, verbose_name='Номер телефона')
    name = models.CharField(max_length=250, verbose_name='Название')
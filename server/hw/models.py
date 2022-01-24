from django.db import models


class First(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(verbose_name='Название', max_length=150)
    type = models.CharField(verbose_name='Тип судна', max_length=150)




class Second(models.Model):
    id = models.AutoField(primary_key=True)
    destination = models.CharField(verbose_name='Пункт назначения', max_length=150)
    load = models.CharField(verbose_name='груз', max_length=150)
    fk = models.ForeignKey('First', on_delete=models.CASCADE)


from django.db import models

# Create your models here.

class Employees(models.Model):
    user = models.CharField('Сотрудник:', max_length=300)
    email = models.EmailField('Email сотрудника:', default=None)
    is_active_status = models.BooleanField('Активен',default=True,)

    def __str__(self):
        return '%s' % self.user

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Equipment(models.Model):
    inventory_number = models.IntegerField('Инвентарный номер:')
    user = models.ForeignKey('Employees', blank=True, null=True, default="Склад")
    name = models.TextField('Оборудование:',max_length=300)
    is_active = models.BooleanField('Активен:',default=True,)



    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Обрудование'






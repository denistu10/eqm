from django.db import models

# Create your models here.

class Users(models.Model):
    name_employee = models.CharField('Имя Фамилия сотрудника:', max_length=300)
    email = models.EmailField('Email сотрудника:', default=None)
    is_active_status = models.BooleanField('Активен',default=True,)

    def __str__(self):
        return '%s' % self.name_employee

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Equipment(models.Model):
    inventory_number = models.IntegerField('Инвентарный номер:')
    name = models.TextField('Оборудование:',max_length=300)
    user = models.ForeignKey('Users', name='Сотрудник:')
    is_active = models.BooleanField('Активен:',default=True,)


    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Обрудование'






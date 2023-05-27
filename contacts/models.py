from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator


class Category(models.Model):
    #Категория формы обратной связи
    title = models.CharField('Категория', max_length= 60)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class ContactForm(models.Model):
    name = models.CharField(verbose_name= 'ФИО', max_length= 60, blank= False)
    full_text = models.TextField('Текст формы', blank= False)
    date = models.DateTimeField('Время отправки формы', default=timezone.now)
    idcategory = models.ForeignKey(
            Category, verbose_name= 'Категория формы', 
            on_delete= models.SET_NULL, null= True)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(verbose_name= 'Номер телефона', null = True, validators = [phoneNumberRegex], max_length = 16, blank=True)
    email = models.EmailField(verbose_name= 'email', max_length=254,  null= True)
    state = models.BooleanField(verbose_name= 'Состояние', default= False)

    def __str__(self):
        return self.name #метод, который определяет как будет и вывыводит информацию
    
    class Meta:
        verbose_name = 'Форма Обратной Связи'
        verbose_name_plural = 'Формы Обратной Связи'

from django.db import models


class Answer(models.Model):
    title = models.CharField('Название', max_length= 50)
    anons = models.CharField('Вопрос', max_length= 250)
    full_text = models.TextField('Ответ')


    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = 'Вопрос-ответ'
        verbose_name_plural = 'Вопросы-ответы'
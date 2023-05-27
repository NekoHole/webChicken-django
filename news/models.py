from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.CharField('Название', max_length= 50)
    anons = models.CharField('Анонс', max_length= 250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')
    images = models.ImageField('Изображение', upload_to= 'news_img/')

    def __str__(self):
        return self.title #метод, который определяет как будет и вывыводит информацию
    
    def get_absolute_url(self):
        return f'/news/{self.id}'
    

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
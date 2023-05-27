from django.db import models

class Category(models.Model):
    #Категории
    title = models.CharField('Категория', max_length= 60)
    url = models.SlugField(max_length= 160, unique= True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Type(models.Model):
    #Типы
    title = models.CharField('Тип', max_length= 60)
    url = models.SlugField(max_length= 160, unique= True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

class Tag(models.Model):
    #Тэги
    title = models.CharField('Тэг', max_length= 60)
    url = models.SlugField(max_length= 160, unique= True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

class Product(models.Model):
    #Продукт
    name = models.CharField('Название', max_length= 100)
    description_text = models.TextField('Описание')
    idcategory = models.ForeignKey(
        Category, verbose_name= 'Категория', on_delete= models.SET_NULL, null= True,
        related_name='products'
        )
    idtype = models.ForeignKey(
        Type, verbose_name= 'Тип', on_delete= models.SET_NULL, null= True,
        related_name='products'
        )
    tag = models.ManyToManyField(Tag,  verbose_name='тэги')
    mainimage = models.ImageField('Основное Изображение', upload_to= 'production_img/')
    storage = models.CharField('Условия Хранения', max_length= 600)
    compound = models.CharField('Состав', max_length= 600)
    cooking = models.CharField('Способ Приготовления', max_length= 600)
    value = models.CharField('Пищевая и Энергетическая ценность', max_length= 200)
    package = models.CharField('Вид Упаковки', max_length= 400)
    url = models.SlugField(max_length= 160, unique= True) 

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class Image(models.Model):
    #Изображения
    title = models.CharField('Название', max_length= 60)
    images = models.ImageField('Изображение', upload_to= 'production_img/')
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete= models.CASCADE)

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


# Create your models here.

# Generated by Django 4.1.7 on 2023-05-11 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Категория')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Тэг')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Тип')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Типы',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description_text', models.TextField(verbose_name='Описание')),
                ('mainimage', models.ImageField(upload_to='production_img/', verbose_name='Основное Изображение')),
                ('storage', models.CharField(max_length=600, verbose_name='Условия Хранения')),
                ('compound', models.CharField(max_length=600, verbose_name='Состав')),
                ('cooking', models.CharField(max_length=600, verbose_name='Способ Приготовления')),
                ('value', models.CharField(max_length=200, verbose_name='Пищевая и Энергетическая ценность')),
                ('package', models.CharField(max_length=400, verbose_name='Вид Упаковки')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('idcategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='production.category', verbose_name='Категория')),
                ('idtype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='production.type', verbose_name='Тип')),
                ('tag', models.ManyToManyField(to='production.tag', verbose_name='тэги')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Название')),
                ('images', models.ImageField(upload_to='production_img/', verbose_name='Изображение')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]

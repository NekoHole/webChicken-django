# Generated by Django 4.1.7 on 2023-05-08 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='images',
            field=models.ImageField(default=1, upload_to='news_img/', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]
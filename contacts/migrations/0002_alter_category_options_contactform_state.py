# Generated by Django 4.1.7 on 2023-05-15 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AddField(
            model_name='contactform',
            name='state',
            field=models.BooleanField(default=False, verbose_name='Состояние'),
        ),
    ]

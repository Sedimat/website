# Generated by Django 4.2.7 on 2023-11-23 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='poster',
            field=models.URLField(default='https://ecopolitic.com.ua/wp-content/uploads/2021/06/shutterstock_1017466240-900x300.jpg'),
        ),
    ]

# Generated by Django 4.2.7 on 2023-12-12 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar2',
            field=models.ImageField(default='avatar.png', upload_to='avatar'),
        ),
    ]
# Generated by Django 4.2.7 on 2023-12-12 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_userprofile_avatar2'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='post.png', upload_to='img_post'),
        ),
    ]

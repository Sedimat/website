# Generated by Django 4.2.7 on 2023-11-23 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_category_options_alter_post_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coments',
            name='post_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='Пост'),
        ),
    ]

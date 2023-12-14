from django.utils import timezone
from django.contrib.auth.models import AbstractUser

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Teg(models.Model):
    name = models.CharField(max_length=30, verbose_name="Назва")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name="Назва")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"


class Post(models.Model):
    title = models.CharField(max_length=30, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Опис")
    published_date = models.DateTimeField(auto_created=True, verbose_name="Час")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    tegs = models.ManyToManyField(Teg, blank=True, related_name='posts', verbose_name="Теги")
    img = models.ImageField(upload_to='img_post', default='post.png')
    poster = models.URLField(
        default="https://ecopolitic.com.ua/wp-content/uploads/2021/06/shutterstock_1017466240-900x300.jpg",
        verbose_name="Постер")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Пости"


class Coments(models.Model):

    coment_date = models.DateTimeField(auto_created=True, verbose_name="Час", default=timezone.now)
    coment = models.TextField(verbose_name="Коментар")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Пост", default=1)

    def __str__(self):
        return self.coment

    class Meta:
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"

class Mailing(models.Model):
    email = models.EmailField(verbose_name="Емейл")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Емейл"
        verbose_name_plural = "Емейли"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Користувач")
    avatar = models.URLField(
        default="https://riotpixels.net/wp/wp-content/uploads/2019/06/Cyberpunk-2077_10-06-19.png",
        verbose_name="аватар")
    avatar2 = models.ImageField(upload_to='avatar',  default='avatar.png')
    description = models.TextField(verbose_name="Опис")

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = "Користувач"
        verbose_name_plural = "Користувачі"





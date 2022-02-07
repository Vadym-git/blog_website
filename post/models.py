from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Categories(models.Model):
    name = models.CharField(verbose_name='Category name', max_length=32, blank=False, null=False)
    reg_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name


class Author(models.Model):
    user = models.OneToOneField(User, blank=False, null=False, on_delete=models.CASCADE)
    nickname = models.CharField(verbose_name='Nickname', max_length=8, blank=False, null=False)
    description = models.TextField(verbose_name='Author description', blank=True)
    reg_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'author'

    def __str__(self):
        return self.nickname


class Post(models.Model):
    author = models.ForeignKey(Author, blank=False, null=True, on_delete=models.SET_NULL)
    header = models.CharField(verbose_name='Header', max_length=96, blank=False, null=False)
    banner = models.ImageField(verbose_name='Picture', upload_to='posts-cover', blank=True, null=True)
    text = models.TextField(verbose_name='Post text')
    category = models.ManyToManyField(Categories)
    is_active = models.BooleanField(verbose_name='Is active', default=False)
    reg_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'posts'

    def __str__(self):
        return self.header

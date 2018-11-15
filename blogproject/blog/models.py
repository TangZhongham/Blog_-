from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    # 分类
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    # 标签
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    # 标题
    title = models.CharField(max_length=100)

    # 正文
    body = models.TextField()

    # 创建、修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # 摘要
    excerpt = models.CharField(max_length=200, blank=True)

    # 关联以上分类与标签
    category = models.ForeignKey(Category)
    tag = models.ManyToManyField(Tag, blank=True)

    # Django 自带用户系统
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk':self.pk})
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models
from blog.models import Post
# Create your models here.


class Comment(models.MODEL):
    post = models.ForeignKey(Post, verbose_name='文章')
    nickname = models.CharField(max_length=50, verbose_name='昵称')
    email = models.EmailField(max_length=254, verbose_name='邮箱')
    website = models.URLField(verbose_name='网站地址')
    content　= models.CharField(max_length=2000, verbose_name='评论内容')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plual = '评论'


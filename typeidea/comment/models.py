# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models

# Create your models here.


class Comment(models.MODEL):
    title = models.ForeignKey()
    username = models.CharField(max_length=50, blank=True, verbose_name='用户名')
    email = models.EmailField(max_length=254, verbose_name='邮箱')
    url = models.URLField(verbose_name='网站地址')
    content　= models.TextField(max_length=300, verbose_name='评论内容')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    user = models.ForeignKey(User, verbose_name='作者')

    class Meta:
        verbose_name = verbose_name_plual = '评论'


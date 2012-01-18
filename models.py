# -*- coding: UTF-8 -*-
from django.db import models
 
# Create your models here.
class SpPages(models.Model):
    title = models.CharField(max_length = 300, verbose_name= (u'Название ПС')) # заголовок для поисковика
    description = models.CharField(max_length = 255, blank=True, verbose_name=(u'Описание ПС')) # описание для поисковиков
    keywords = models.CharField(max_length = 255, blank=True, verbose_name=(u'Ключевые слова ПС')) # описание для поисковиков
    header = models.TextField(verbose_name=(u'Название для людей')) # заголовок для новости
    content = models.TextField(verbose_name=(u'Cодержание')) #  подробное содержимое новости
    catkey = models.ForeignKey('SpPages', verbose_name=(u'Раздел'), blank=True, null=True)
 
    def __unicode__(self):
        result = self.title
        return result
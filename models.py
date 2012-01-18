# -*- coding: UTF-8 -*-
from django.db import models
 
# Create your models here.
class SpPage(models.Model):
    title = models.CharField(max_length = 300, verbose_name= (u'Название ПС'))
    description = models.CharField(max_length = 255, blank=True, verbose_name=(u'Описание ПС'))
    keywords = models.CharField(max_length = 255, blank=True, verbose_name=(u'Ключевые слова ПС')) 
    header = models.CharField(max_length = 300, verbose_name=(u'Название для людей'), blank=True) 
    content = models.TextField(verbose_name=(u'Cодержание'))
    menuname = models.CharField(max_length = 300, verbose_name= (u'Название в меню'), blank=True)
    menustatus = models.BooleanField(verbose_name=(u'Отображать в меню'))
    aliasname = models.CharField(max_length = 300, verbose_name= (u'ЧПУ')) 
    catkey = models.ForeignKey('SpPage', verbose_name=(u'Раздел'), blank=True, null=True)
 
    def __unicode__(self):
        result = self.title
        return result
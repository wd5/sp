# -*- coding: UTF-8 -*-
from django.db import models
 
# Create your models here.
class SpPage(models.Model):
    Title = models.CharField(max_length = 300, verbose_name= (u'Название ПС'))
    Header = models.CharField(max_length = 300, verbose_name=(u'Название для людей'), blank=True, null=True)
    Description = models.CharField(max_length = 255, verbose_name=(u'Описание ПС'), blank=True, null=True)
    keywords = models.CharField(max_length = 255, verbose_name=(u'Ключевые слова ПС'), blank=True, null=True)
    IntroText = models.TextField(verbose_name=(u'Аннотация (введение)'), blank=True, null=True)
    Content = models.TextField(verbose_name=(u'Cодержание'))
    MenuName = models.CharField(max_length = 300, verbose_name= (u'Название в меню'), blank=True, null=True)
    MenuStatus = models.BooleanField(verbose_name=(u'Отображать в меню'))
    AliasName = models.CharField(max_length = 300, verbose_name= (u'ЧПУ')) 
    CatKey = models.ForeignKey('SpPage', verbose_name=(u'Раздел'), blank=True, null=True)
    VisibleStatus = models.BooleanField(verbose_name=(u'Опубликован'))
    SearchEnginesStatus = models.BooleanField(verbose_name=(u'Доступ для ПС'))
    DeleteStatus = models.BooleanField(verbose_name=(u'Удален в корзину'))
    PubDateStart = models.DateTimeField(verbose_name=(u'Дата публикации'), blank=True, null=True)
    PubliDateStop = models.DateTimeField(verbose_name=(u'Дата отмены публикации'), blank=True, null=True)
    Position = models.IntegerField(verbose_name=(u'Позиция или приоритет'), blank=True, null=True)
    Thumbs = models.ImageField(upload_to='thumbs', verbose_name=(u'Миниатюра'), blank=True, null=True)
    Attachment = models.FileField(upload_to='files', verbose_name=(u'Прикрепленный файл'), blank=True, null=True)
 
    def __unicode__(self):
        result = self.Title
        return result
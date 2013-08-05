# -*- coding: utf-8 -*-
from django.db import models


class Member(models.Model):
    name = models.CharField(u'ФИО', max_length=64)
    slug = models.SlugField()
    position = models.CharField(u'Должность', max_length=64)
    email = models.EmailField(blank=True)
    tel = models.CharField(u'Телефоны', max_length=255, help_text=u'Запятая заменяется на перевод строки', blank=True)
    about = models.TextField(u'Инфо')
    photo = models.ImageField(u'Фото', upload_to='photo', help_text=u'Размер 200 на 200 px')
    is_active = models.BooleanField(u'Показывать на сайте', default=True)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_ajax_link(self):
        return (
            'team_get_member', (), {'pk': self.id}
        )


    @property
    def tel_list(self):
        return self.tel.split(',')

    @property
    def get_articles(self):
        return self.publication_set.filter(is_active=True, category__is_interview=False)

    @property
    def get_interview(self):
        return self.publication_set.filter(is_active=True, category__is_interview=True)

    class Meta:
        verbose_name = u'Член команды'
        verbose_name_plural = u'Команда'


class Publication(models.Model):
    author = models.ForeignKey('Member', verbose_name=u'Автор')
    category = models.ForeignKey('Category', verbose_name=u'Категория')
    title = models.CharField(u'Заголовок статьи', max_length=128)
    short_text = models.TextField(u'Анонс')
    text = models.TextField(u'Текст публикации')
    create_date = models.DateField(auto_now_add=True)
    image = models.ImageField(u'Изображение', upload_to='publication')
    slug = models.SlugField()
    is_active = models.BooleanField(u'Показывать на сайте', default=True)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return (
            'team_publication_item', (), {'slug': self.slug}
        )

    class Meta:
        verbose_name = u'Публикация'
        verbose_name_plural = u'Публикации'


class Category(models.Model):
    title = models.CharField(u'Название категории', max_length=64)
    slug = models.SlugField()
    is_interview = models.BooleanField(u'Это интервью', default=False, help_text=u'Отметить если в этой категории публикуются только интервью')
    is_active = models.BooleanField(u'Показывать на сайте', default=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'


# -*- coding: UTF-8 -*-
from django.contrib import admin
from . import models as m
from django import forms
from tinymce.widgets import TinyMCE


class PublicationAdminForm(forms.ModelForm):
    class Meta:
        model = m.Publication
        widgets = {
            'text': TinyMCE(attrs={'cols': 90, 'rows': 30},),
        }


class PublicationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('create_date', 'title', 'category', 'is_active', 'is_top')
    list_display_links = ('title',)
    list_filter = ('category', 'is_active', 'is_top')
    search_fields = ('title', 'short_text', 'text')
    radio_fields = {"category": admin.VERTICAL}
    form = PublicationAdminForm


admin.site.register(m.Publication, PublicationAdmin)
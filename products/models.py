from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Category(models.Model):
    title=models.CharField(_('title'),max_length=55)
    description=models.TextField(_(' description'),blank=True)
    avatar=models.ImageField(_('avatar'),blank=True)
    is_enable=models.BooleanField(_('is_enable'),default=True)
    created_time=models.DateTimeField(_('created_time'),auto_now_add=True)
    updated_time=models.DateTimeField(_(' updated_time'),auto_now=True)
    class Meta:
        db_table='categories'
        verbose_name='category'
        verbose_name_plural = 'Categories'

class Product(models.Model):
    title=models.CharField(_('title'),max_length=55)
    description=models.TextField(_(' description'),blank=True)
    avatar=models.ImageField(_('avatar'),blank=True)
    is_enable=models.BooleanField(_('is_enable'),default=True)
    categories=models.ManyToManyField('Category',verbose_name=_('categories'),blank=True)
    created_time = models.DateTimeField(_('created_time'), auto_now_add=True)
    updated_time = models.DateTimeField(_(' updated_time'), auto_now=True)
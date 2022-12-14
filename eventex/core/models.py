from django.db import models
from django.shortcuts import resolve_url as r

from eventex.core.managers import KindQuerySet, PeriodManager


# Create your models here.
class Speaker(models.Model):
    name = models.CharField('Nome', max_length=255)
    slug = models.SlugField()
    website = models.URLField('Website', blank=True)
    photo = models.URLField('Foto', )
    description = models.TextField('Descrição', blank=True)

    class Meta:
        verbose_name = 'palestrante'
        verbose_name_plural = 'palestrantes'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('speaker_detail', slug=self.slug)


class Contact(models.Model):
    EMAIL = 'E'
    PHONE = 'P'

    KINDS = (
        (EMAIL, 'E-mail'),
        (PHONE, 'Telefone'),
    )
    speaker = models.ForeignKey('Speaker', on_delete=models.CASCADE, verbose_name='palestrante')
    kind = models.CharField('Tipo', max_length=1, choices=KINDS)
    value = models.CharField('valor', max_length=255)

    objects = KindQuerySet.as_manager()

    class Meta:
        verbose_name = 'contato'
        verbose_name_plural = 'contatos'

    def __str__(self):
        return self.value


class Talk(models.Model):
    title = models.CharField('Título', max_length=200)
    start = models.TimeField('Início', null=True, blank=True)
    description = models.TextField('Descrição', blank=True)
    speakers = models.ManyToManyField('Speaker', verbose_name='palestrantes', blank=True)

    objects = PeriodManager()
    class Meta:
        verbose_name = 'palestra'
        verbose_name_plural = 'palestras'

    def __str__(self):
        return self.title

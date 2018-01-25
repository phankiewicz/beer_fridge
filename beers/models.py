from django.db import models
from django.utils.translation import ugettext_lazy as _

from stdimage.models import StdImageField
from stdimage.utils import UploadToClassNameDir


class BeerType(models.Model):
    name = models.CharField(
        _('beer type'),
        max_length=64,
    )
    serving_temperature = models.FloatField(
        _('serving temperature'),
    )

    class Meta:
        verbose_name = _('beer type')
        verbose_name_plural = _('beer types')
        ordering = ('id',)

    def __str__(self):
        return f'{self.name}'


class Beer(models.Model):
    name = models.CharField(
        _('name'),
        max_length=64,
    )
    type = models.ForeignKey(
        BeerType,
        verbose_name=_('type'),
        related_name='beers',
    )
    image = StdImageField(
        _('image'),
        upload_to=UploadToClassNameDir(),
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _('beer')
        verbose_name_plural = _('beers')
        ordering = ('id',)

    def __str__(self):
        return f'{self.name}'


class FridgeShelf(models.Model):
    beer = models.ForeignKey(
        Beer,
        verbose_name=_('beer'),
        related_name='shelves',
    )
    current_temperature = models.FloatField(
        _('current temperature'),
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _('fridge shelf')
        verbose_name_plural = _('fridge shelves')
        ordering = ('id',)

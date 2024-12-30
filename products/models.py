from django.db import models

from helpers.image import resize_image


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    short_description = models.CharField(max_length=255, verbose_name='Descrição curta')
    long_description = models.TextField(verbose_name='Descrição longa')
    image = models.ImageField(
        upload_to='products/%Y/%m/%d/', blank=True, verbose_name='Imagem'
    )
    slug = models.SlugField(unique=True, verbose_name='Slug')
    marketing_price = models.FloatField(verbose_name='Preço de marketing')
    promotional_marketing_price = models.FloatField(
        default=0, verbose_name='Preço de marketing promocional'
    )
    product_type = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variável'),
            ('S', 'Simples'),
        ),
        verbose_name='Tipo do produto',
    )

    def save(self, *args, **kwargs) -> None:
        if self.image:
            resize_image(self.image, is_saved=False)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'


class Variation(models.Model):
    product = models.ForeignKey(Product, models.CASCADE, verbose_name='Produto')
    name = models.CharField(max_length=255, blank=True, verbose_name='Nome')
    price = models.FloatField(verbose_name='Preço')
    promotional_price = models.FloatField(default=0, verbose_name='Preço promocional')
    stock = models.PositiveIntegerField(default=1, verbose_name='Estoque')

    def __str__(self) -> str:
        return self.name or self.product.name

    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'

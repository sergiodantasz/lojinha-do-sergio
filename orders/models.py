from django.contrib.auth.models import User
from django.db import models

from products.models import Variation


class Order(models.Model):
    user = models.ForeignKey(User, models.CASCADE, verbose_name='Usuário')
    total_value = models.FloatField(verbose_name='Valor total')
    status = models.CharField(
        max_length=1,
        default='C',
        choices=(
            ('C', 'Criado'),
            ('P', 'Pendente'),
            ('A', 'Aprovado'),
            ('R', 'Reprovado'),
            ('E', 'Enviado'),
            ('F', 'Finalizado'),
        ),
        verbose_name='Status',
    )

    def __str__(self) -> str:
        return f'Pedido #{self.pk}'

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'


class Item(models.Model):
    order = models.ForeignKey(Order, models.CASCADE, verbose_name='Pedido')
    # TODO: When the variation is deleted, keep its information stored in the item.
    variation = models.ForeignKey(
        Variation, models.SET_NULL, null=True, verbose_name='Variação'
    )
    price = models.FloatField(verbose_name='Preço')
    promotional_price = models.FloatField(default=0, verbose_name='Preço promocional')
    image = models.CharField(max_length=100, blank=True, verbose_name='Imagem')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Quantidade')
    # TODO: When the product is approved, leave all information static.

    def __str__(self) -> str:
        return self.variation.__str__()

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'

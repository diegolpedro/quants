import datetime
from django.db import models


class CotizacionActual(models.Model):
    symbol = models.CharField(max_length=255, primary_key=True)
    settlement = models.CharField(max_length=255)
    last = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    change = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    open = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    high = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    low = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    previous_close = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    turnover = models.BigIntegerField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    operations = models.IntegerField(blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    expiration = models.DateField(blank=True, null=True)
    strike = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    kind = models.TextField(blank=True, null=True)
    underlying_asset = models.TextField(blank=True, null=True)
    panel = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # No permite que Django maneje la tabla
        db_table = 'cotizacion_actual'  # Nombre exacto de la tabla en la BD
        constraints = [
            models.UniqueConstraint(
                fields=['symbol', 'settlement'], name='unique_symbol_settlement_combination'
            )
        ]
        
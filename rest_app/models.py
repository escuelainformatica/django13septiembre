from django.db import models

# Create your models here.
class Factura(models.Model):
    cliente:str=models.CharField(max_length=50)
    # detallefacturas
    # detallefactura_set (list detallefactura)


class DetalleFactura(models.Model):
    descripcion:str=models.CharField(max_length=50)
    cantidad:int=models.IntegerField()
    precio_unitario:int=models.IntegerField()
    idfactura:int=models.ForeignKey(Factura,on_delete=models.CASCADE,related_name="detallefacturas")


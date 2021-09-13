from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre:str=models.CharField(max_length=50)
    direccion:str=models.CharField(max_length=50)

class Factura(models.Model):
    # cliente:str=models.CharField(max_length=50)
    idcliente:int=models.ForeignKey(Cliente,on_delete=models.CASCADE,related_name="cliente",null=True)
    # detallefactura_set (list detallefactura)


class DetalleFactura(models.Model):
    descripcion:str=models.CharField(max_length=50)
    cantidad:int=models.IntegerField()
    precio_unitario:int=models.IntegerField()
    idfactura:int=models.ForeignKey(Factura,on_delete=models.CASCADE,related_name="detallefacturas")



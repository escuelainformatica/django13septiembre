import json

from django.forms import model_to_dict
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from rest_app.models import Factura


def listarFacturas(request):
    # .prefetch_related('detallefacturas') leer los campos relacional que falta
    # .select_related('detallefacturas')  Lee un campo relacional que falta
    query=Factura.objects.prefetch_related('detallefacturas').all() # dos queryset
    listadoFacturas=list(query.values()) # listado [ {dict.},{dict}]
    posicion=0
    for valor in query:
        listadoFacturas[posicion]["cliente"]=model_to_dict(valor.idcliente)
        listadoFacturas[posicion]['detallefacturas']=list(valor.detallefacturas.all().values())
        posicion=posicion+1

    # resultado=list(Factura.objects.all()) # devuelvo el listado comun una consulta (query)
    return JsonResponse(listadoFacturas,safe=False)

def obtenerFactura(request,id):
    # .select_related('detallefacturas')
    tmp=Factura.objects.prefetch_related('detallefacturas').get(id=id) # queryset
    resultado1=model_to_dict(tmp) # convierto la factura en un diccionario (no incluye detallefacturas)
    resultado1["cliente"]=model_to_dict(tmp.idcliente)
    resultado1["detallefacturas"]=list( tmp.detallefacturas.all().values())
    return JsonResponse(resultado1, safe=False)

@csrf_exempt # <--- @algo antes de una clase o funcion es un decorador.
def guardarFactura(request):
    nuevo=json.loads(request.body) # diccionario {id:1,nombre:"fact"}

    # facturanueva=Factura("id":1,"nombre":"fact")

    facturanueva=Factura(**nuevo) # objeto (** kwargs)
    Factura.save(facturanueva) # guardar en la base de datos

    return JsonResponse(nuevo, safe=False)
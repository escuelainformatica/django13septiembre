import json

from django.forms import model_to_dict
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from rest_app.models import Factura


def listarFacturas(request):
    resultado1=list(Factura.objects.all().values())
    # resultado=list(Factura.objects.all()) # devuelvo el listado comun una consulta (query)
    return JsonResponse(resultado1,safe=False)

def obtenerFactura(request,id):
    resultado1=model_to_dict(Factura.objects.get(id=id))
    return JsonResponse(resultado1, safe=False)

@csrf_exempt # <--- @algo antes de una clase o funcion es un decorador.
def guardarFactura(request):
    nuevo=json.loads(request.body) # diccionario {id:1,nombre:"fact"}

    # facturanueva=Factura("id":1,"nombre":"fact")

    facturanueva=Factura(**nuevo) # objeto (** kwargs)
    Factura.save(facturanueva) # guardar en la base de datos

    return JsonResponse(nuevo, safe=False)
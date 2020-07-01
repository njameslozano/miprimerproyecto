from django.shortcuts import render, HttpResponse, redirect
from .models import Factores, Sintomas

# Create your views here.

def index(request):
    lista_factores = Factores.objects.values('id','nombre')
    lista_sintomas = Sintomas.objects.values('id','nombre')
    context = { "factores" : lista_factores,
                "sintomas" : lista_sintomas,
                "numero_de_factores" : len(lista_factores), 
                "numero_de_sintomas" : len(lista_sintomas) }

    return render(request,"index.html",context )



def contacto(request):
    return render(request,"contacto.html")



def detalle(request):
    id_factor = request.GET.get('idfactor','')
    if id_factor == '':
        return redirect('index')
    else:
        try:
            factor = Factores.objects.get(id=id_factor)
        except Factores.DoesNotExist:
            factor = ''
        if factor == '':
            return redirect('index')
        else:
            context = {"nombrefactor":factor.nombre,
                    "detalle":factor.información}
            return render(request,"detalle.html", context)


def detalledos(request):
    id_sintoma = request.GET.get('idsintoma','')
    if id_sintoma == '':
        return redirect('index')
    else:
        try:
            sintoma = Sintomas.objects.get(id=id_sintoma)
        except Sintomas.DoesNotExist:
            sintoma = ''
        if sintoma == '':
            return redirect('index')
        else:
            context2 = {"nombresintoma":sintoma.nombre,
                        "detalle":sintoma.información}
            return render(request,"detalledos.html",context2)
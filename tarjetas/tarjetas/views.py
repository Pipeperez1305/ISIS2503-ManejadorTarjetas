from tarjetas.forms import  TarjetaForm
from .models import Tarjeta
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
import json

def TarjetaList(request):
    queryset = Tarjeta.objects.all()
    context ={
        'tarjeta_list': queryset} #list(queryset.values('id', 'tipo', 'puntaje'))
    return render(request, 'Tarjeta/tarjetas.html', context)

def TarjetaCreate(request):
    if request.method == 'POST':
        form = TarjetaForm(request.POST)
        if form.is_valid():
            tarjeta=form.save()
            tarjeta.save()
            messages.add_message(request, messages.SUCCESS,'Tarjeta creada exitosamente')
            return HttpResponseRedirect(reverse('tarjetaCreate'))
        else:
            print(form.errors)
        
    else:
        form = TarjetaForm()
    
    context={'form': form} 
    
        # data = request.body.decode('utf-8')
        # data_json = json.loads(data)
        # tarjeta = Tarjeta()
        # tarjeta.tipo = data_json["tipo"]
        # tarjeta.puntaje = data_json["puntaje"]
        # tarjeta.save()
    return render(request, 'Tarjeta/tarjetaCreate.html', context)

def TarjetaUpdate(request, id):
    tarjeta = Tarjeta.objects.get(id=id)
    
    if request.method == 'POST':
        form = TarjetaForm(request.POST, instance=tarjeta)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,'Tarjeta actualizada exitosamente')
            return HttpResponseRedirect(reverse('tarjetaList'))
        else:
            print(form.errors)
    else:
        form = TarjetaForm(instance=tarjeta)
        
    return render(request, 'Tarjeta/tarjetaUpdate.html', {'form': form})
    
def getTarjetaList(request):
    if request.method == 'GET':
        queryset = Tarjeta.objects.all()
        context = list(queryset.values('id', 'tipo', 'puntaje'))
        return JsonResponse(context, safe=False)
    
def getTarjeta(request, id):
    if request.method == 'GET':
        tarjeta = Tarjeta.objects.get(id=id)
        context = {'id': tarjeta.id, 'tipo': tarjeta.tipo, 'puntaje': tarjeta.puntaje}
        return JsonResponse(context, safe=False)
    
def deleteTarjeta(request, id):
    if request.method == 'POST':
        tarjeta = Tarjeta.objects.get(id=id)
        tarjeta.delete()
        return HttpResponseRedirect(reverse('tarjetaList'))
    else:
        return HttpResponse('No se pudo eliminar la tarjeta')
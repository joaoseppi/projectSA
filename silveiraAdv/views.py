from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('HOME TEST')


def contato(request):
    return HttpResponse('CONTATO')


def sobre(request):
    return HttpResponse('SOBRE')

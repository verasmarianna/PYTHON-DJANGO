from pickletools import read_int4
from django.shortcuts import render

def index(request):
    return render(request, 'gallery/index.html')

def imagem (request):
    return render (request, 'gallery/imagem.html')

def imagem2 (request):
    return render (request, 'gallery/imagem2.html')

def imagem3 (request):
    return render (request, 'gallery/imagem3.html')

def imagem4 (request):
    return render (request, 'gallery/imagem4.html')

def imagem5 (request):
    return render (request, 'gallery/imagem5.html')

def imagem6 (request):
    return render (request, 'gallery/imagem6.html')


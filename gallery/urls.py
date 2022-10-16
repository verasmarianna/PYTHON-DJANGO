from django.urls import path
from gallery.views import index, imagem, imagem2, imagem3, imagem4, imagem5, imagem6

urlpatterns = [
    path ('', index),
    path ('imagem/', imagem, name='imagem'),
    path ('imagem2/', imagem2, name='imagem2'),
    path ('imagem3/', imagem3, name='imagem3'),
    path ('imagem4/', imagem4, name='imagem4'),
    path ('imagem5/', imagem5, name='imagem5'),
    path ('imagem6/', imagem6, name='imagem6'),
]
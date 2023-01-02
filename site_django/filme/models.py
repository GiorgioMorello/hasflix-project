from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Create movies


LISTA_CATEGORIAS = (
    ('ANALISE', 'Análise'),
    ('PROGRAMACAO', 'Programação'),
    ('APRESENTACAO', 'Apresentação'),
    ('OUTRO', 'Outro'),
)


class Filme(models.Model):
    titulo = models.CharField(max_length=40)
    descricao = models.TextField(max_length=1200)
    categoria = models.CharField(choices=LISTA_CATEGORIAS, max_length=30)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)
    thumb = models.ImageField(upload_to='thumb_filmes')

    def __str__(self):
        return self.titulo


# Create EP

class Episodio(models.Model):
    filme = models.ForeignKey('Filme', related_name='episodios', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=90)
    video = models.URLField()

    def __str__(self):
        return self.titulo


class Usuario(AbstractUser):
    filme_vistos = models.ManyToManyField('Filme')

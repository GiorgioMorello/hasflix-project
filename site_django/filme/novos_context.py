from .models import Filme



def lista_filmes_recentes(r):
    lista_filmes = Filme.objects.all().order_by('-data_criacao') #Lista python
    return {'filmes_recentes': lista_filmes}



def lista_filmes_alta(r):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes') #Lista python
    return {'filmes_alta': lista_filmes}



def filme_destaque(r):
    filme_d = Filme.objects.order_by('-visualizacoes').first() # É um objeto só
    return {'filme_d': filme_d}
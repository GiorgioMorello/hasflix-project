from django.urls import path, include, reverse_lazy
from .views import Homepage, Homefilmes, DetatlhesFilme, PesquisaFilme, PaginaPerfil, CriarConta
from django.contrib.auth import views as auth_view



app_name = 'filme'
urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('filmes/', Homefilmes.as_view(), name='home_filmes'),
    path('filmes/<int:pk>', DetatlhesFilme.as_view(), name='detalhes_filme'),
    path('pesquisa/', PesquisaFilme.as_view(), name='pesquisa_filme'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('pagina-perfil/<int:pk>', PaginaPerfil.as_view(), name='pagina_perfil'),
    path('criar-conta/', CriarConta.as_view(), name='criar_conta'),
    path('alterar-senha/', auth_view.PasswordChangeView.as_view(
        template_name='pagina_perfil.html', success_url=reverse_lazy('filme:homefilmes')), name='alterar_senha'),
]


from django.shortcuts import render, redirect, reverse
from .models import Filme, Usuario
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CriarContaForm, HomeForm

class Homepage(FormView):
    template_name = 'homepage.html'
    form_class = HomeForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('filme:home_filmes')
        return super().get(request, *args, **kwargs)


    def get_success_url(self):
        email_homepage = self.request.POST.get('email')
        usuarios = Usuario.objects.filter(email=email_homepage)

        if usuarios:
            return reverse('filme:login')
        self.request.session['email_homepage'] = email_homepage # Passando email para sessão
        return reverse('filme:criar_conta')







class Homefilmes(LoginRequiredMixin, ListView):
    template_name = 'homefilmes.html'
    model = Filme
    # object_list -> lista de itens do modelo




class DetatlhesFilme(LoginRequiredMixin, DetailView):
    template_name = 'detalhes_filmes.html'
    model = Filme

    # Contabilizando uma visualização sempre que o usuário acessar a página do filme
    def get(self, request, *args, **kwargs):
        # Descobrir qual filme ele ta acessando
        filme = self.get_object()

        # Add +1 na visualização do filme
        filme.visualizacoes += 1
        filme.save()
        # Redireciona o usuário para a url final

        #  Registrando Filme Visto
        usuario = request.user
        usuario.filme_vistos.add(filme)

        return super(DetatlhesFilme, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DetatlhesFilme, self).get_context_data(**kwargs)
        # Filtrar a tabela de filmes pegando os filmes cuja a categoria é igual a categoria do object
        # Para pegar o object usamos a função get_object -> é o filme
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)  # é uma lista python
        context['filmes_relacionados'] = filmes_relacionados
        return context
    # object -> um item do modelo





class PesquisaFilme(LoginRequiredMixin, ListView):
    template_name = 'pesquisa.html'
    model = Filme

    def get_queryset(self):
        filme_pesquisa = self.request.GET.get('query')
        if filme_pesquisa:
            object_list = self.model.objects.filter(titulo__icontains=filme_pesquisa)
            return object_list

        else:
            return None





class PaginaPerfil(LoginRequiredMixin, UpdateView):
    template_name = 'pagina_perfil.html'
    model = Usuario
    fields = ['email', 'first_name', 'username']


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Vai pegar o ultimo caractere, que no caso é o id do usuário
        context['url'] = int(self.request.path[-1])
        return context


    def get_success_url(self):
        return reverse('filme:home_filmes')




class CriarConta(FormView):
    template_name = 'criar_conta.html'
    form_class = CriarContaForm  # Este formulario esta criando um item no nosso BD


    def form_valid(self, form):
        form.save()

        return super().form_valid(form)  # Vai retornar a função 'get_success_url' ou seja vai me redirecionar para página de login


    def get_success_url(self):  # O que vai acontecer se o formulário for bem sucedido.
        return reverse('filme:login')
    # Essa função espera um link como resposta, queremos retornar o link que corresponde ao link do filme login



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        email_homepage = self.request.session.get('email_homepage') # Pegando o email que foi passado na sessão
        context['form']['email'].initial = email_homepage # Colocando o email no formulário de email
                                # O initial serve como value do input
        return context


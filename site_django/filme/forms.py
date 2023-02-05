from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms
from django.utils.translation import gettext_lazy as _



class HomeForm(forms.Form):
    email = forms.EmailField(required=True, label=False, widget=forms.EmailInput(attrs={'class': 'home_input'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #print(self.fields['email'].widget.attrs)


class CriarContaForm(UserCreationForm):

    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'email_field'}))

    class Meta:
        model = Usuario


        fields = ['username', 'email', 'password1', 'password2'] # Essa tupla vai dizer quais são os campos que vão ser exibidos no formulario

        help_texts = {
            'username': _('Nome de usuário não pode conter apenas números'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Removendo os help_text dos inputs
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''



from django import forms
from models import Aluno

class AlunoRegistrationForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'idade', 'turma']
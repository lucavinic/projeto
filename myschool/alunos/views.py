from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from forms import AlunoRegistrationForm

def register_aluno(request):
    if request.method == 'POST':
        form = AlunoRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin:index')
    else:
        form = AlunoRegistrationForm()

    return render(request, 'alunos/register_aluno.html', {'form': form})
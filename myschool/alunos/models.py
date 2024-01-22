from django.db import models

# Create your models here.
from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    turma = models.CharField(max_length=10)

    def __str__(self):
        return self.nome

class Nota(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    disciplina = models.CharField(max_length=100)
    valor = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.aluno.nome} - {self.disciplina}"
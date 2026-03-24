from django.db import models


class Curso(models.Model):
    codigo = models.CharField(max_length=5, unique=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} ({self.codigo})"


class Student(models.Model):
    nome = models.CharField(max_length=50)
    cursoId = models.ForeignKey(Curso)
    matricula = models.PositiveBigIntegerField(unique=True)

    def __str__(self):
        return f"{self.nome} ({self.curso.nome})"

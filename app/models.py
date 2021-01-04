from django.db import models
from datetime import datetime


class Cliente(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome completo do cliente')
    endereco = models.CharField(max_length=100, help_text='Ex: Nome da rua, número - Cidade, UF, CEP')
    telefone = models.CharField(max_length=14, help_text='formato: (+55) + número do código da região + número telefônico')
    data_nascimento = models.DateField(help_text='formato: YYYY-MM-DD')
    data_cadastro = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.nome
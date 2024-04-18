from django.db import models

class Produto(models.Model):
    NomeProduto = models.CharField(max_length = 100, blank = False)
    Descricao = models.TextField(blank = True)
    Preco = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    Estoque = models.DecimalField(max_digits=10, decimal_places=2, blank=False)

    def __str__(self):
        return self.Title

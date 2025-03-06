from django.db import models
from django.contrib.auth.models import User



# Modelo de Produto (Estoque)
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome

# Modelo de Comanda
class Comanda(models.Model):
    STATUS_CHOICES = [
        ('aberta', 'Aberta'),
        ('fechada', 'Fechada')
    ]
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cliente = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='aberta')
    data_criacao = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Comanda {self.id} - {self.cliente or 'Sem cliente'}"

    def calcular_total(self):
        """Calcula o total da comanda com base nos itens."""
        return sum(item.calcular_total() for item in self.itens.all())

# Modelo de Itens da Comanda
class ItemComanda(models.Model):
    comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE, related_name="itens")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def calcular_total(self):
        return self.quantidade * self.produto.preco  # Supondo que 'preco' exista em Produto

from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    preco = models.FloatField(null=False, blank=False)
    imagem = models.ImageField(upload_to='media/burguer', default='', null=False, blank=False)

    def __str__(self):
        return self.nome

from django.db import models

# Create your models here.


class Pessoas (models.Model):
    nome = models.CharField(max_length=50,default='none')
    idade=models.IntegerField()
    raiva=models.IntegerField()

    def __str__(self):
        return self.nome
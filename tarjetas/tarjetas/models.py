from django.db import models

class Tarjeta(models.Model):
    tipo = models.CharField(max_length=50, null=False)
    puntaje = models.IntegerField(null=False)   
    

    def __str__(self):
        return '{}'.format(self.tipo)
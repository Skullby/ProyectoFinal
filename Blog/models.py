from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=40)
    cuerpo = models.TextField()
    autor = models.CharField(max_length=40)

    def __str__(self):
        return self.titulo + "|" + self.autor
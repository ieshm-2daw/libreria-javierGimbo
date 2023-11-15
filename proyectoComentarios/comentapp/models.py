from django.conf import settings
from django.db import models



class Comentario(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()



    def __str__(self):
        return self.title
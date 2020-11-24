from django.db import models

# Create your models here.

class Podaci(models.Model):
    uslov = models.BooleanField()
    tacka = models.CharField(max_length=200)
    poligon = models.CharField(max_length=200)

    def __str__(self):
        if self.uslov:
            return f"Tačka {self.tacka} pripada poligonu {self.poligon}"
        else:
            return f"Tačka {self.tacka} ne pripada poligonu {self.poligon}"
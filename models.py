from django.db import models

class Factores(models.Model):
    nombre = models.CharField(max_length=100)
    información = models.TextField()

    def publish(self):
        self.save()


class Sintomas(models.Model):
    nombre = models.CharField(max_length=100)
    información = models.TextField()

    def publish(self):
        self.save()
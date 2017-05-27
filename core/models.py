from django.db import models

class Operation(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return 'Operation: '+self.name

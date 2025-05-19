from django.db import models
class FbModel(models.Model):
    name=models.CharField(max_length=30)
    Class=models.IntegerField()
    feedback=models.TextField()
    def __str__(self):
        return self.name
# Create your models here.

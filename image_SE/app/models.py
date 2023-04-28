from django.db import models

class Query(models.Model):
    id=models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='upload/')
    k = models.CharField(max_length=100)


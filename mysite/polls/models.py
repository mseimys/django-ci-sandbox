from django.db import models

class Poll(models.Model):
    a = models.IntegerField(default=0)

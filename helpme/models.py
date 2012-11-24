from django.db import models

class Point(models.Model):
    id = models.AutoField(primary_key=True)
    lat = models.FloatField()
    lng = models.FloatField()
    state = models.SmallIntegerField(default=0)

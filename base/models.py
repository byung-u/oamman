from django.db import models

class Banner(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=128, null=True, blank=True)
    #image = SorlImageField(upload_to='banner')
    desc = models.CharField(max_length=128, null=True, blank=True)

    begin = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)

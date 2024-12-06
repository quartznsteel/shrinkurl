from django.db import models

# URL Pair model, constructed automatically with migrate functions

class URLPair(models.Model):
    long_url = models.CharField(max_length=500)
    short_url = models.CharField(max_length=200)

    def __str__(self):
        return self.short_url

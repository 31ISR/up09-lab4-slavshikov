from django.db import models

class Communitie(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    free = models.BooleanField(default=True)





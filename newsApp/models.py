from django.db import models

class Post(models.Model):
    idd = models.TextField() 
    desc = models.TextField()
    news = models.TextField()
    img = models.TextField()

class Saved(models.Model):
    idd = models.TextField()
    desc = models.TextField()
    news = models.TextField()
    img = models.TextField()
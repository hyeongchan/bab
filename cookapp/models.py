from django.db import models

class Post(models.Model):
    objects = models.Manager()
    code = models.IntegerField(null=True)
    name = models.CharField(max_length=10, null=True)
    category = models.CharField(max_length = 10, null=True)
    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=255, null=True)
    url = models.URLField(null=True)
    image = models.ImageField(upload_to='images/', null=True)
    ingredients = models.ManyToManyField(Post)
    def __str__(self):
        return self.name
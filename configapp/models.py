from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Movie(models.Model):
    title = models.CharField(max_length=150)
    year = models.IntegerField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    genre = models.CharField(max_length=50)
    actor = models.ManyToManyField('Actor')


    def __str__(self):
        return self.title


class Actor(models.Model):
    name = models.CharField(max_length=150)
    birthdate = models.DateField()

    def __str__(self):
        return self.name


class CommitMovie(models.Model):
    title = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_ed = models.DateField(auto_now_add=True)
    update_ed = models.DateTimeField(auto_now=True)


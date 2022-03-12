from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.DurationField(null=True, blank=True, verbose_name='Durations')
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, related_name='reviews')

    def __str__(self):
        return self.movie.title


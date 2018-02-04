from django.db import models

class Schedule(models.Model):
    date = models.DateTimeField()
    start_at = models.DateTimeField()
    title = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title

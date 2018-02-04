from django.db import models

class Schedule(models.Model):
    date = models.DateField()
    start_at = models.TimeField()
    title = models.CharField(max_length=200)
    member = models.CharField(max_length=200, null=True)
    text = models.TextField()
    place = models.CharField(max_length=200,)

    def __str__(self):
        return self.title

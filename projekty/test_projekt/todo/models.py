from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

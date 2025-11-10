from django.db import models


class Language(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.CharField(max_length=200)

    def __str__(self):
        return self.title

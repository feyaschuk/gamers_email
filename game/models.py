from django.db import models


class Game(models.Model):
    email = models.EmailField()
    date_of_entry = models.DateTimeField(auto_now_add=True)

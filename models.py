from django.db import models


class Message(models.Model):
    content = models.TextField()
    # sender = models.ForeignKey(User)
    # receiver = models.ForeignKey(User)
    
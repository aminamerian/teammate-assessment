from datetime import datetime
from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    weight = models.SmallIntegerField(default=1)

    def __str__(self):
        return self.title


class Reply(models.Model):
    RATE = (('Good', 2), ('Medium', 1), ('Bad', 0))

    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='replies')
    rate = models.SmallIntegerField(choices=RATE)
    voter = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name='replies_voter')
    candidate = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name='replies_candidate')
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f''

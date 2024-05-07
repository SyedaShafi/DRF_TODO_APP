from django.db import models
from django.contrib.auth.models import User
# Create your models here.
OPTIONS = (
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
)
class Task (models.Model):
    user = models.ForeignKey(User, blank = True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    due_date = models.DateField(blank=True, null=True)
    priority = models.CharField(choices=OPTIONS, max_length=100, blank=True, null=True)
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title
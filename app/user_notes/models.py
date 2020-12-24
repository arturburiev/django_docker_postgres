from django.db import models
from django.conf import settings
from django.utils import timezone


class Note(models.Model):
    title = models.CharField('Title', max_length=40)
    text = models.CharField('Text', max_length=255)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    created_at = models.DateTimeField('CREATED_AT', default=timezone.now)

    class Meta:
        db_table = "notes"
        ordering = ['-created_at']

    def __str__(self):
        return self.title + ' - ' + self.text

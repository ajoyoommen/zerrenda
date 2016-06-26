from django.db import models
from django.utils import timezone


class TimeStampedModel(models.Model):
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        super(TimeStampedModel, self).save(*args, **kwargs)

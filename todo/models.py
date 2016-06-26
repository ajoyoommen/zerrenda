from django.db import models
from django.utils.text import slugify

from common.models import TimeStampedModel


class List(TimeStampedModel):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(List, self).save(*args, **kwargs)

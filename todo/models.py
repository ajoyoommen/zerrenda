from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

from common.models import DeleteSafeTimeStampedMixin


class List(DeleteSafeTimeStampedMixin):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50, editable=False)
    author = models.ForeignKey(User, related_name="lists_authored")

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(List, self).save(*args, **kwargs)


class Item(DeleteSafeTimeStampedMixin):
    list = models.ForeignKey(List, related_name="items")
    name = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    author = models.ForeignKey(User, related_name="items_authored")

    def __unicode__(self):
        return self.name

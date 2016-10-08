from django.db import models
from django.utils import timezone


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        super(TimeStampedModel, self).save(*args, **kwargs)


class SoftDeleteMixin(models.Model):
    delete = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def delete(self, force=False):
        if force:
            super(SoftDeleteMixin, self).delete()
        else:
            self.delete = True
            self.save()

    def save(self, undelete=False, *args, **kwargs):
        if undelete:
            self.delete = False
        super(SoftDeleteMixin, self).save(*args, **kwargs)


class DeleteSafeTimeStampedMixin(SoftDeleteMixin, TimeStampedMixin):
    class Meta:
        abstract = True

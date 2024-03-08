from django.db import models
from apps.common.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Brand(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


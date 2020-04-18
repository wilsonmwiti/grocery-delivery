from django.db import models


class PaymentsBaseModel(models.Model):
    confirmation_status = models.BooleanField(default=False)

    class Meta:
        abstract = True

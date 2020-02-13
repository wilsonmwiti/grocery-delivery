from django.db import models

# Create your models here.


class Payments(models.Model):
    pass
    # class Meta:
    #     db_table = "payments"
    #     verbose_name_plural = "payments"


class Sales(models.Model):
    time_sold = models.DateTimeField(auto_now_add=True)
    payment_id = models.ForeignKey(Payments, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'sales'
        verbose_name_plural = 'sales'

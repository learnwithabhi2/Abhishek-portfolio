from django.db import models

# Create your models here.
from django.db import models

class JobOffer(models.Model):
    company_name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    package = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
    notice_period = models.CharField(max_length=50)
    work_location = models.CharField(max_length=100)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company_name} - {self.designation}"

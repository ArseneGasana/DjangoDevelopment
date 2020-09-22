from django.db import models

class teacher (models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    briefSummary = models.TextField()

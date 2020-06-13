from django.db import models
from django.utils import timezone

# Create your models here.
class Diary(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    publish_date = models.DateTimeField(default=timezone.now)
    content = models.TextField()

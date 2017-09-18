from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
# Create your models here.

class New (models.Model):
    unique_id = models.CharField(max_length=10, primary_key=True, default='')
    user = models.CharField(max_length=50, default='')
    title        =  models.CharField(max_length=200, default='')
    content      =  models.TextField(null=True)
    image_link   = models.TextField(null=True)
    created_date =  models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return "/detail/%s/" %(self.unique_id)

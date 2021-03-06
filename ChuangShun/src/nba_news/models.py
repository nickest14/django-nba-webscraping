from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save


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


def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    print( instance.unique_id )
    print( instance.title)
    print( '\n' )


post_save.connect(post_save_user_receiver, sender=New)

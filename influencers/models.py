from django.db import models

class Influencer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    instagram_handle = models.CharField(max_length=30, blank=True, null=True)
    youtube_channel = models.CharField(max_length=255, blank=True, null=True)
    twitter_handle = models.CharField(max_length=30, blank=True, null=True)
    facebook_page = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

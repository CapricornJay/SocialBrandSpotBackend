from django.db import models

# Create your models here.

from influencers.models import Influencer
from brands.models import Brand

class Collaboration(models.Model):
    influencer = models.ForeignKey(Influencer, on_delete=models.CASCADE, related_name='collaborations')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='collaborations')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

class CollaborationRequest(models.Model):
    influencer = models.ForeignKey(Influencer, on_delete=models.CASCADE, related_name='collaboration_requests')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='collaboration_requests')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

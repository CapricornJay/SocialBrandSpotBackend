from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    website = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

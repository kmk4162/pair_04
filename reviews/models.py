from django.db import models
from django.conf import settings

class Comment(models.Model):
    # review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()

class Review(models.Model):
    pass

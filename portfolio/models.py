from django.db import models
class project(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    image=models.ImageField(upload_to='potfolio/image/')
    url=models.URLField(blank=True)



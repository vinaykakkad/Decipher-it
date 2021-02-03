from django.db import models


class Events(models.Model):

    title = models.CharField(max_length=256, blank=False)
    description = models.TextField(blank=False)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    video = models.FileField(null=True, blank = True, upload_to='videos')
    image = models.FileField(null=True, blank = True, upload_to='images')
    slug = models.SlugField(max_length=200, unique=True)
    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return self.title



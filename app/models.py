from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_date = models.DateTimeField("created date")

class Author(models.Model):
    username = models.CharField(max_length=12)
    blog_count = models.SmallIntegerField()
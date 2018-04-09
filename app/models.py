from django.db import models
from django.utils import timezone

class Blog(models.Model):
    DRAFT = 1
    PUBLISHED = 2
    ARCHIVED = 3

    STATUS = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
        (ARCHIVED, 'Archived')
    )

    title = models.CharField(max_length=100)
    body = models.TextField(blank=True)
    slug = models.CharField(max_length=100)
    snippet = models.TextField(max_length=128, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(null=True)
    status = models.SmallIntegerField(choices=STATUS, default=1)
    rating = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('app.views.blog_entry', args=[str(self.slug)])

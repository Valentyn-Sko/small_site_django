from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=120, blank=False, db_index=True)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=120, blank=False, db_index=True)

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

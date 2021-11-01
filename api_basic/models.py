from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return self.title

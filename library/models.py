from django.db import models
from django.conf import settings


# Create your models here.
class Book(models.Model):
    Category = (
        ('Science', 'Science'),
        ('Fiction', 'Fiction'),
        ('Mystery', 'Mystery'),
    )
    title = models.CharField(max_length=100, blank=False)
    book_category = models.CharField(max_length=20, choices=Category)
    is_issued = models.BooleanField(default=False, blank=True, null=True)
    issued_to = models.CharField(max_length=30, blank=True, null=True)
    due_date = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.title

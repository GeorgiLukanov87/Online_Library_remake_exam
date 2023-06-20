from django.db import models


# Profile model

class ProfileModel(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image_url = models.URLField()


# Book model
class BookModel(models.Model):
    CHOICES = (
        ('1.Fantasy', 'Fantasy'),
        ('2.Roman', 'Roman'),
        ('3.Study', 'Study'),
        ('4.Modern', 'Modern'),
        ('5.Horror', 'Horror'),
    )
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=250)
    image = models.URLField()
    type = models.CharField(
        max_length=20,
        choices=CHOICES,
    )


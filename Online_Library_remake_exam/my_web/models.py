from django.db import models


# Profile model
class ProfileModel(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image_url = models.URLField()


# Book model
class BookModel(models.Model):
    CHOICES = (
        ('Fiction', '1.Fiction'),
        ('Novel', '2.Novel'),
        ('Crime', '3.Crime'),
        ('Fantasy', '4.Fantasy'),
        ('Roman', '5.Roman'),
        ('Study', '6.Study'),
        ('Modern', '7.Modern'),
        ('Horror', '8.Horror'),
    )

    title = models.CharField(max_length=30)
    description = models.TextField(max_length=250)
    image = models.URLField()
    type = models.CharField(
        max_length=20,
        choices=CHOICES,
    )

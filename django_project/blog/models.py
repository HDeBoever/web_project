from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your database models here. Tables for users, but posts also.
# Django has a built in authentication system, as well as user model.

# Each class is its own table in the database

# Creating the model for posts
class Post(models.Model):
    # title field is a character field with a restriction of 100 characters in length
    title = models.CharField(max_length = 100)

    # Unrestricted in length
    content = models.TextField()

    # Date is the date of the post when the post was created
    date_posted = models.DateTimeField(default = timezone.now)

    # Author field. Users author posts. 1 to many relationship. If a user is deleted, also delete their post.
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

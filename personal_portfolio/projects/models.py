from django.db import models


# Create your models here.
from django.db.models import CharField


class Projects(models.Model):
    title = models.CharField(max_length=144)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="https://images.unsplash.com/photo-1612151855475-877969f4a6cc?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8aGQlMjBpbWFnZXxlbnwwfHwwfHw%3D&w=1000&q=80")

    def __str__(self) -> CharField:
        return self.title

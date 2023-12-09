from django.db import models

# Create your models here.


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    project_date = models.DateTimeField(max_length=200)
    project_operator = models.CharField(max_length=200)

    def __str__(self):
        return self.project_name


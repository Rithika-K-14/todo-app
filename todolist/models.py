from django.db import models


class TodoListItem(models.Model):
    content = models.TextField() 
    choices = models.CharField(max_length=20, default="personal")



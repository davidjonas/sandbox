from django.db import models

class EditableBlock(models.Model):
    id = models.SlugField(max_length=100, primary_key=True)
    content = models.TextField()
    last_modified = models.DateField(auto_now=True)
    
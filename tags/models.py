from django.db import models
from django.contrib.contenttypes.models import ContentType # ContentType is a model that represents type of an object in our application 
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length=255)

class TaggedItem(models.Model):
    # what tag applied to what items
    # For defining the Generic Relationship we need two information: 1- Type(product, video, article) 2- ID
    # Using the type we can find the table and usinf the ID we can find the record


    tag = models.ForeignKey(to=Tag, on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField() # ID: every table has a postive primary key
    content_object = GenericForeignKey() # Using this field, we can read the actual object that the tag is applied to.


from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True) #creates a field storing characters, max length is 128
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __unicode__(self): #unicode method provides a unicode representation of model instance
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category) #creates one-to-many relationship with model/table category
    title = models.CharField(max_length=128)
    url = models.URLField() #field storing url
    views = models.IntegerField(default=0,unique=False) #field to store integers

    def __unicode__(self):
        return self.title
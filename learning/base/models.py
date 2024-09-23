from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey('Topic', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    #participants
    # participants = models.ManyToManyField('auth.User', related_name='participants')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
# creating new class with MESSAGE!
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # on deleting the parent child will also be deleted!
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    
    body = models.TextField()
    updated = models.DateField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.body[0:50] # only first 50 chars!
    
# created another model named Message: where learned about 
# one to many relations and also used foreign key!!
# created another model named Topic and added it to Room model as foreign key!
# also register both new models in admin admin.site.register(...)!
# also display them in a view!
# creating the form for create room and creating view for it and also created the url!
# created a basic form using forms.ModelForm and learned about fields in details! 
# used this form and created a view for it and also handled the post of this methods!
# url for handling update_room, then created a view for it and also handled the post of this methods!
# also get to know how to update data having filled with previous state of the data!
# also created a delete form for the room and the redirect back to the rooms page !

class Topic(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
       return self.name
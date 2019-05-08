from django.db import models

# Create your models here.

class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()
class League(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()
class Drive(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()
class Game(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()    
class Player(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()
class Trait(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()
class PositionUnit(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()
class Play(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()  
'''
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
'''
class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'subject', 'body', 'pk')

from django.db import models

# Create your models here.

class Topic(models.Model):
	topic_name = models.CharField(max_length=264,unique=True)

	def __str__(self):
		return self.topic_name

class Entry(models.Model):
	entry = models.ForeignKey(Topic,on_delete=models.CASCADE)
	text = models.CharField(max_length=500 , unique=True)

	def __str__(self):
		return self.text
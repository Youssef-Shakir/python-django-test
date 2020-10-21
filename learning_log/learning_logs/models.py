from django.db import models

# Create your models here.

class topic(models.Model):
	text = models.CharField(max_length=200)
	data_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.text
class entry(models.Model):
	topic = models.ForeignKey(topic , on_delete=models.CASCADE)
	text = models.TextField()

class Meta:
	verbose_name_plural = 'entry'
	def __str__(self):
		return f"{self.text[:50]}..."
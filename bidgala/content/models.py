from django.db import models

class Content(models.Model):
	subject = models.CharField(max_length=100, blank=False)
	text = models.TextField(blank=True)
	location = models.TextField(blank=True)
	author = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return self.subject

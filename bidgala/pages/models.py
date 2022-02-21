from django.db import models


def path_edit(instance, filename):
	return '/'.join(['homepage', str(instance.id) + '_' +  filename])


class HomePage(models.Model):
	image = models.ImageField(upload_to=path_edit, blank=False)
	value = models.CharField(max_length=100, blank=False)
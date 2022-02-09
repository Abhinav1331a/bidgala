from django.db import models

# Create your models here.

def path_edit(instance, filename):
	return '/'.join(['user_preference_survey', str(instance.id) + '_' +  filename])


def path_edit_size(instance, filename):
	return '/'.join(['user_preference_size_survey', str(instance.id) + '_' +  filename])


def path_edit_category(instance, filename):
	return '/'.join(['user_preference_category_survey', str(instance.id) + '_' +  filename])


def path_edit_style(instance, filename):
	return '/'.join(['user_preference_style_survey', str(instance.id) + '_' +  filename])


class UserPreference(models.Model):
	image = models.ImageField(upload_to=path_edit, blank=False)
	value = models.CharField(max_length=100, blank=False)


class UserPreferenceCategory(models.Model):
	image = models.ImageField(upload_to=path_edit_category, blank=False)
	value = models.CharField(max_length=100, blank=False)


class UserPreferenceStyle(models.Model):
	image = models.ImageField(upload_to=path_edit_style, blank=False)
	value = models.CharField(max_length=100, blank=False)


class AdvisoryPageData(models.Model):
	category_sculpture = models.BooleanField(default=False)
	category_photography = models.BooleanField(default=False)
	category_drawing = models.BooleanField(default=False)
	category_painting = models.BooleanField(default=False)

	style_abstract = models.BooleanField(default=False)
	style_blackAndWhite= models.BooleanField(default=False)
	style_figurative = models.BooleanField(default=False)
	style_landscape = models.BooleanField(default=False)
	style_minimalist = models.BooleanField(default=False)
	style_popArt = models.BooleanField(default=False)
	style_portraiture = models.BooleanField(default=False)
	style_street = models.BooleanField(default=False)
	style_other = models.BooleanField(default=False)

	preferred_pieces = models.CharField(max_length=1000, null=True)

	orientation_horizontal = models.BooleanField(default=False)
	orientation_vertical = models.BooleanField(default=False)
	orientation_square = models.BooleanField(default=False)

	size_oversize = models.BooleanField(default=False)
	size_large = models.BooleanField(default=False)
	size_medium = models.BooleanField(default=False)
	size_small = models.BooleanField(default=False)

	budget = models.FloatField(default=0.0)

	firstName = models.CharField(max_length=100, null=False)
	lastName = models.CharField(max_length=100, null=True)
	email = models.CharField(max_length=100, null=True)
	phone = models.CharField(max_length=100, null=True)
	notes = models.CharField(max_length=10000, null=True)

	newsletterSubscription =  models.BooleanField(default=False)



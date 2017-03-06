from django.db import models
from django.utils import timezone

class currency(models.Model):
	text = models.CharField(max_length=3)
	def __str__(self):
		return self.text

class broker(models.Model):
	name = models.CharField(max_length=255)
	url = models.CharField(max_length=255)
	def __str__(self):
		return self.name

class brokeraccount(models.Model):
	broker    = models.ForeignKey('adm.broker')
	number    = models.CharField(max_length=32)
	password  = models.CharField(max_length=255)
	server    = models.CharField(max_length=255)
	type      = models.CharField(max_length=255)
	currency  = models.ForeignKey('adm.currency')
	def __str__(self):
		return self.number
		
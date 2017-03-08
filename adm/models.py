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

class broker_account(models.Model):
	broker    = models.ForeignKey('adm.broker')
	number    = models.CharField(max_length=32)
	password  = models.CharField(max_length=255)
	server    = models.CharField(max_length=255)
	type      = models.CharField(max_length=255)
	currency  = models.ForeignKey('adm.currency')
	def __str__(self):
		return self.number

class invest_date(models.Model):
	year = models.IntegerField()
	week = models.IntegerField()
	def __str__(self):
		return "%0.2d/%4d" % (self.week,self.year)

class entry_code(models.Model):
  text = models.CharField(max_length=32)
  def __str__(self):
    return self.text


class user_account(models.Model):
  user = models.ForeignKey('auth.user')
  code = models.ForeignKey('adm.entry_code')
  amount = models.DecimalField(max_digits=20,decimal_places=4)
  invest_date = models.ForeignKey('adm.invest_date')
  text = models.CharField(max_length=255,blank=True)
  balance = models.DecimalField(max_digits=20,decimal_places=4,default=0)
  def __str__(self):
    return str(self.id)


class invest_plan(models.Model):
  invest_date = models.ForeignKey('adm.invest_date')
  broker_account = models.ForeignKey('adm.broker_account')
  balance_in = models.DecimalField(max_digits=20,decimal_places=4)
  balance_out = models.DecimalField(max_digits=20,decimal_places=4)
  open_pl = models.DecimalField(max_digits=20,decimal_places=4)
  close_pl = models.DecimalField(max_digits=10,decimal_places=4,default=0)
  dd = models.DecimalField(max_digits=10,decimal_places=4,default=0)
  def __str__(self):
    return str(self.invest_date)

class user_profile(models.Model):
  user = models.OneToOneField('auth.user')
  referral = models.ForeignKey('auth.user', related_name='referral',default=1)
  einlage = models.DecimalField(max_digits=20,decimal_places=2,default=0)
  auszahlung = models.DecimalField(max_digits=20,decimal_places=2,default=0)
  profit = models.DecimalField(max_digits=4,decimal_places=1,default=0.5)
  balance = models.DecimalField(max_digits=20,decimal_places=2,default=0)
  deposit = models.DecimalField(max_digits=20,decimal_places=2,default=0)
  currency = models.ForeignKey('adm.currency')
  invest_date = models.DateField(blank=True)
  pay_date = models.DateField(blank=True)
  days = models.IntegerField()
  def __unicode__(self):
    return self.user.username
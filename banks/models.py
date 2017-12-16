# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Bank(models.Model):
	name = models.CharField(max_length=50)
	id = models.AutoField(primary_key=True)

	def __str__(self):
		return str(self.id) + '-' + self.name

	def serialize(self):
		return {
			'id': self.id,
			'name': self.name
		}

class Branch(models.Model):
	ifsc = models.CharField(max_length=11, primary_key=True)
	bank = models.ForeignKey(Bank)
	branch = models.CharField(max_length=100)
	address = models.CharField(max_length=500)
	city = models.CharField(max_length=50)
	district = models.CharField(max_length=50)
	state = models.CharField(max_length=50)

	def __str__(self):
		return self.ifsc + '-' + self.branch + '-' + self.city + '-' + self.state

	def serialize(self):
		return {
			'ifsc': self.ifsc,
			'bank': self.bank.name,
			'branch': self.branch,
			'address': self.address,
			'city': self.city,
			'district': self.district,
			'state': self.state
		}

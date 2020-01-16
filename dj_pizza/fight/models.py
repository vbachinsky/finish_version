from __future__ import unicode_literals
from django.db import models
import random


WARRIORS = [
	('strong', 'Strong'),
	('healthy', 'Healthy'),
	('skill', 'Skill'),
]

BATTLE = [
	('head', 'head'),
	('body', 'body'),
	('foot', 'foot'),
]


class Warrior(models.Model):
	name = models.CharField(null=False, max_length=50)
	description = models.CharField(null=False, max_length=10, choices=WARRIORS)
	power = models.FloatField(default=10)
	health = models.FloatField(default=100)
	skill = models.FloatField(default=1.0)

	def set_warrior(self):
		if self.description == 'strong':
			self.power = self.power * 1.5
		if self.description == 'healthy':
			self.health = self.health * 1.5
		if self.description == 'skill':
			self.skill = self.skill * 1.5
		self.save()

		class Meta:
			abstract = True


class Fight(Warrior):
	kick = models.CharField(null=False, max_length=10, choices=BATTLE)
	block = models.CharField(null=False, max_length=10, choices=BATTLE)

	def get_damage(self):
		return (self.power * self.skill)

	def __str__(self):
		return 'Warrior: {}, power: {}, health: {}, skill: {}, name: {}'.format(str(self.description), str(self.power), str(self.health), str(self.skill), str(self.name))

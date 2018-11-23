import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Game(models.Model):
	def __str__(self):
		return self.game_name

	game_name = models.CharField(max_length=50)
	min_player_count = models.IntegerField(default=4)
	max_player_count = models.IntegerField(default = 0)

class Rule(models.Model):
	def __str__(self):
		return self.rule_name

	rule = models.ForeignKey(Game, on_delete=models.CASCADE)
	rule_name = models.CharField(max_length=50)
	rule_text = models.CharField(max_length=280)
	rule_order = models.IntegerField(default=0)

class FAQ(models.Model):
	def __str__(self):
		return self.faq_name

	faq_name = models.CharField(max_length=50)
	faq_text = models.CharField(max_length=280)
	order = models.IntegerField(default=1)
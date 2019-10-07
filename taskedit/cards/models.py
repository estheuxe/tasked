from django.db import models

class Card(models.Model):
	card_id_in_service = models.CharField(max_length=100)
	card_name = models.CharField(max_length=50, help_text="Title of Card")
	card_description = models.TextField(help_text="Description")
	card_type = models.CharField(max_length=20)

	def __str__(self):
		return self.card_name
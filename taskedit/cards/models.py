from django.db import models

class Card(models.Model):
	name = models.CharField(max_length=50, help_text="Title of Card")
	desc = models.TextField(help_text="Description")
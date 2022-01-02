from django.db import models



class ToDo(models.Model):

	# class model for todo app
	text = models.CharField(max_length=500)

	def __str__(self):
		return text_added
		

from django.db import models



class ToDo(models.Model):

	# class model for todo app
	text_added = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return text_added

	class Meta:
		ordering = ['-date_added']
		

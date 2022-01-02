from .models import ToDo
from django.forms import ModelForm
from django import forms


class ToDoForm(ModelForm):
	class Meta:
		model = ToDo
		fields = "__all__"


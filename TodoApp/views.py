from django.shortcuts import render, redirect
from .models import ToDo
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.utils import timezone


# Create your views here.


def index(request):
	todo_text = ToDo.objects.all()
	if request.method == 'POST':
		new_todo = ToDo(
			text = request.POST.get('title', False)
			)
		new_todo.save()
		return redirect('/')
	return render(request, 'index.html', {'todo_text': todo_text})




"""
@csrf_exempt
def add_todo(request):
	current_date = timezone.now()
	content = request.POST.get("content")
	created_obj = ToDo.objects.create(
		added_date=current_date,
		text=content
		)
	length_of_todos = ToDo.objects.all().count()
	return HttpResponseRedirect("/")

@csrf_exempt
def delete_todo(request):
	if request.method == 'POST':
		todo_obj = ToDo.objects.get(pk=todo_id) # getting an object from the id taken from the url
		todo_obj.delete()

	return redirect('index')
"""
 

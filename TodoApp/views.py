from django.shortcuts import render
from .models import ToDo

# Create your views here.


def index(request):
	todo = ToDo.objects.all()
	context = {'todo': todo}
	return render(request, 'index.html', context)


def add_todo(request):
	if request.method == 'POST':
		text_added = request.POST['text_added']
		ToDo.objects.create(text_added= text_added)
		# saves a ToDo to the model ToDo
	return redirect('index')

def delete_todo(request):
	if request.method == 'POST':
		todo_obj = ToDo.objects.get(pk=todo_id) # getting an object from the id taken from the url
		todo_obj.delete()

	return redirect('index')

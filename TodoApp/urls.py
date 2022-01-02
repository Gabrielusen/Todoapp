from django.urls import path
from .views import index, add_todo, delete_todo


urlpatterns = [
	path('', index, name='index'),
	path('add_todo', add_todo, name='add_todo'),
	path('delete_todo/<int:todo_id', delete_todo, name='delete_todo'),
]
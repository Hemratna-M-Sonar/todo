
from django.urls import path
from . import views
urlpatterns = [
    path('',views.listview,name='listview'),
    path('inserttode',views.inserttodo,name="inserttodo"),
    path('delete_todo_item/<int:todo_id>/',views.delete_todo_item,name="delete_todo_item"),
]

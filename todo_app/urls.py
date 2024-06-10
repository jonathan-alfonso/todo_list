from django.urls import path
from todo_app import views

urlpatterns = [
    path("", views.TodoListView.as_view(), name="index"),
    path("list/<int:list_id>", views.ItemListView.as_view(), name="list"),
]
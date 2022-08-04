from django.urls import path
from .views import TodoList,TodoDetail,home

urlpatterns = [
    path("<int:pk>/",TodoDetail.as_view()),
    path("", TodoList.as_view()),
    path("home/", home,name='homepage')
]
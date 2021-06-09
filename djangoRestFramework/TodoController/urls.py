from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name = 'ApiOverview'),
    path('getall', views.TodoList, name = 'TodoList'),
    path('<str:pk>', views.TodoCreate, name = 'TodoCreate'),
    path('get/<str:pk>', views.TodoDetail, name = 'TodoDetail'),
    path('put/<str:pk>', views.TodoUpdate, name = 'TodoUpdate'),
    path('deletet/<str:pk>', views.TodoDelete, name = 'TodoDelete')
]

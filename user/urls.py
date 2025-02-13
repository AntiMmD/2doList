from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('signup/',signUp, name='signup'),
    path('login/', login,  name='login'),
    path('logout/', logout, name='logout'),
    path('home/', home, name ='home'),
    path('add_task/', addTask, name='add_task'),
    path('delete_task/<int:id>/', deleteTask, name='delete_task'),
    path('update_task/<int:id>/', updateTask, name= 'update_task'),
    path('search_task/', searchTask, name= 'search_task')
]

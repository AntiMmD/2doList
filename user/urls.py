from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('signup/',signUp, name='signup'),
    path('login/', login,  name='login'),
    path('logout/', logout),
    path('home/', home ),
    path('add_task/', addTask),
    path('delete_task/<int:id>/', deleteTask),
    path('update_task/<int:id>/', updateTask),
    path('search_task/', searchTask)
]

from django.contrib import admin

from user.models import User
from task.models import Task

class TaskInline(admin.StackedInline):
    model = Task

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_staff', 'is_active']
    list_editable = ['is_staff']
    inlines = [TaskInline]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['user','name','status','priority']
    list_editable = ['priority']
    
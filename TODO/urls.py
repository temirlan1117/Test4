from django.contrib import admin
from django.urls import path
from tasks.views import list_tasks, detail_tasks, create_tasks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', list_tasks),
    path('tasks/<int:task_id>/', detail_tasks),
    path('tasks/create/', create_tasks),
]

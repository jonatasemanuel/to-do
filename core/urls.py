from django.urls import path
from . import views


urlpatterns=[
    path('', views.new_task, name='new_task'),
    path('edit/<int:task_id>',views.edit_task, name='edit_task'),
    path('delete/<int:task_id>', views.delete, name='delete')
]
 
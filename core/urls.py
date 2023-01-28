from django.urls import path
from . import views


urlpatterns=[
    #path('', views.new_task, name='new_task'),
    path('', views.HomeFormView.as_view(), name='home'),
    path('edit/<int:pk>',views.TaskUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete', views.delete, name='delete'),
]
 
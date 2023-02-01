from django.urls import path
from . import views


urlpatterns=[
    path('', views.HomeView.as_view(), name='home'),
    path('edit/<int:pk>',views.TaskUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete', views.TaskDeleteView.as_view(), name='delete'),
]
 
from django.urls import path
from .views import UserListCreateApiView,UserRetrieveUpdateView
from .views import TaskListCreateApi,TaskRetrieveUpdateApiView

urlpatterns=[
    path('users/',UserListCreateApiView.as_view(),name='user_list'),
    path('users/<int:pk>/',UserRetrieveUpdateView.as_view(),name='user-detail'),

    path('tasks/',TaskListCreateApi.as_view(),name='task_list'),
    path('tasks/<int:pk>/',TaskRetrieveUpdateApiView.as_view(),name='task_detail')
]
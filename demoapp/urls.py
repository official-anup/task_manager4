from django.urls import include, path
from . import views
from django.contrib.auth.views import LogoutView



from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, UserViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('register/', views.register, name='register'),

    path('', views.task_list, name='task_list'),
    
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
    
    path('tasks/new/', views.task_create, name='task_create'),
    
    path('tasks/<int:pk>/edit/', views.task_update, name='task_update'),

    path('accounts/logout/', LogoutView.as_view(), name='logout'),

    
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),

     path('api/', include(router.urls)),
]

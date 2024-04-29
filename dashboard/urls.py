from django.urls import path
from . import views
from .views import database_actions, show_database_files, edit_database


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('database-actions/', views.database_actions, name='database_actions'),
    path('show-database-files/', views.show_database_files, name='show_database_files'),
    path('edit-database/', views.edit_database, name='edit_database'),
    path('analytics/', views.analytics_ , name='analytics'),
    path('predictions/', views.predictions_ , name='predictions'),
 
    
]
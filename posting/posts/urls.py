from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/',    views.login_view,    name='login'),
    path('logout/',   views.logout_view,   name='logout'),
    path('',          views.home,          name='home'),
    path('new/',      views.post_create,   name='post-create'),
    path('edit/<int:pk>/',   views.post_update, name='post-update'),
    path('delete/<int:pk>/', views.post_delete, name='post-delete'),
]
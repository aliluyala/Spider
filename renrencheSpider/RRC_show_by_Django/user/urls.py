from django.conf.urls import url

from user import views

urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    # url(r'^all_users/', views.all_users, name='all_users'),
    # url(r'^edit_user/', views.edit_user, name='edit_user'),
    # url(r'^role_permission/', views.role_permission, name='role_permission'),
]
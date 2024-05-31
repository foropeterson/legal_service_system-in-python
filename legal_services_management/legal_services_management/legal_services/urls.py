from django.urls import path
from . import views

urlpatterns = [
    path('cases/', views.case_list, name='case_list'),
    path('cases/create/', views.case_create, name='case_create'),
    path('cases/<int:pk>/update/', views.case_update, name='case_update'),
    path('cases/<int:pk>/delete/', views.case_delete, name='case_delete'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]

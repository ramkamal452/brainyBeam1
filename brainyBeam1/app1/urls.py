from django.urls import path
from . import views
urlpatterns = [
    path('', views.base, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),

    path('registration/', views.registration, name='registration'),

    path('logging/', views.logging, name='logging'),

]

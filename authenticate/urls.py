from . import views
from django.urls import path, include

urlpatterns = [
    path('landing/', views.landing, name='landing'),
    path('login/', views.login_user, name="login"),
    path('logout/',views.logout_user, name='logout'),
    path('register/',views.register_user, name='register'),

]

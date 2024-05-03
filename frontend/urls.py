from django.urls import path
from . import views



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.list, name='list'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='user_login'),
]
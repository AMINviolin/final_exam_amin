from django.urls import path
from .views import Login, Logout, signup


app_name = 'accounts'

urlpatterns = [
    path('login/', Login, name='login2'),
    path('logout/', Logout, name='logout'),
    path('signup/', signup, name='signup'),
]

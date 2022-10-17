from django.urls import path

from .views import home, signup_view, signin_view, room, signout_view

app_name = 'chat'
urlpatterns = [
    path('home/', home, name='home'),
    path('signup/', signup_view, name='signup_namespace'),
    path('signin/', signin_view, name='signin_namespace'),
    path('logout/', signout_view, name='signin_namespace'),
    path('<str:room_name>/', room, name='room'),
]
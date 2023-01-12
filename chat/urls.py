from django.urls import path

from .views import home, signup_view, signin_view, room, signout_view, image_upload_view

app_name = 'chat'

urlpatterns = [
    path('', home, name='home'),
    path('room/<str:room_name>/', room, name='room'),
    path('signup/', signup_view, name='signup_namespace'),
    path('signin/', signin_view, name='signin_namespace'),
    path('signout/', signout_view, name='logout_namespace'),
    path('room/<str:room_name>/image_upload/', image_upload_view),
]

# path('upload/', mongo_image_upload),
# path('<str:room_name>/upload/', mongo_image_upload),
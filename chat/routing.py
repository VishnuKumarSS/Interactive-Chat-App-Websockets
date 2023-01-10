from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chatt/room/(?P<room_name>\w+)/$', consumers.ChatRoomConsumer.as_asgi()), 
]

# here w is match word characters. Match any words with any length ....This match Alphabets Upper and Lower case and numbers..0 to 9 and the underscore...
# here what the w+ do is ...It sends what ever we type on the url...It is going to send that to the consumers.py...
# $ symbol ends the string...
# the room_name is just the naming convention. to name the group. # if we don't use that, then it will be unnamed.

#  \w for word character and \W for non-word character; \d for digit and \D or non-digit.
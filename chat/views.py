import pdb
import traceback
from django.shortcuts import render, redirect
from chat.models import ImageUpload, Messages, Room
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from .forms import ImageForm
from .mongo_models import *
import base64


def home(request):
    """
    Function used for showing landing page of the application.
    
    :param request: HTTP Request
    :return: HTTP Response
    """
    context = {}
    rooms_list = []
    try:
        if request.method == 'POST':
            custom_roomname = request.POST['input_roomname']
            return redirect(f'/chat/room/{custom_roomname}')
        else:
            rooms_list = Room.objects.all()
            context['rooms_list'] = rooms_list        
    except Exception as error:
        print(error)
    return render(request, 'home.html', context)


def room(request, room_name):
    """
    Function that handles all the Chat messages for authorized users.
    
    :param request: HTTP Request
    :return: HTTP Response
    """
    context = {}
    messages = []

    room = Room.objects.filter(name=room_name).first()
    if request.user.is_authenticated:
        if room:
            # messages = Messages.objects.filter(user=request.user, room=room)
            messages = Messages.objects.filter(room=room)
        else:
            room = Room(name=room_name)
            room.save()

    context['room_name'] = room_name
    context['messages'] = messages

    return render(request, 'chatroom.html', context)


def image_upload_view(request, room_name):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance  # it will return the image model object
            # return render(request, 'image_upload.html', {'form': form, 'img_obj': img_obj})
            room_obj = Room.objects.filter(name=room_name).first()
            Messages.objects.create(user=request.user, message=img_obj.title, room=room_obj, image=img_obj)
            return redirect(f'/chat/room/{room_name}/')
    else:
        form = ImageForm()
    return render(request, 'image_upload.html', {'form': form})


def signup_view(request):
    """
    Function that handles all the registration or signup part.
    
    :param request: HTTP Request
    :return: HTTP Response
    """
    context = {}

    if request.user.is_authenticated: # if the user is already authenticated
        return redirect('/chat/home')

    if request.method == 'POST':  # if user filled the form
        form = UserCreationForm(request.POST)  # passing the data's for further use

        if form.is_valid():  # this is the function of above django's UserCreatingForm
            form.save()  # saving form for further use
            username = request.POST['username']  # entered_username
            password = request.POST['password1']  # entered_password
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('/chat/home')

        else:
            print('Form is not valid!')
            return render(request, 'signup.html', {'form': form})
            
    else:
        print('First time opened')
        return render(request, 'signup.html', context)


def signin_view(request):
    """
    Function that handles signing up the users.
    
    :param request: HTTP Request
    :return: HTTP Response
    """
    context = {}
    if request.user.is_authenticated:
        return redirect('/chat/home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/chat/home')
        else:
            return render(request, 'signin.html', context)
    else:
        return render(request, 'signin.html', context)


def signout_view(request):
    """
    Function that handles signing out the users.
    
    :param request: HTTP Request
    :return: HTTP Response
    """
    logout(request)
    return redirect('/chat/home')


# def room(request, room_name):
#     context = {}
#     room = Room.objects.filter(name=room_name).first()
#     # images = ImageUpload.objects.filter(name=room_name).first()
#     all_messages = []
#     all_images = []
#     if request.user.is_authenticated:
#         user = User.objects.get(username=request.user.username)
#         if room:
#             # messages = Messages.objects.filter(room=room).filter(user=user)
#             # other_messages = Messages.objects.filter(room=room).filter(~Q(user=user))
#             all_messages = Messages.objects.filter(room=room)
#             all_images = ImageUpload.objects.filter(room=room).order_by('-id')
#         else:
#             room = Room(name=room_name)
#             room.save()

#     context['room_name'] = room_name
#     context['all_messages'] = all_messages
#     context['all_images'] = all_images
#     # context['image_form'] = image_form
#     # {
#     #     'room_name': room_name,
#     #     'all_messages': all_messages,
#     #     'image_form': image_form,
#     # }
#     return render(request,'chatroom.html',context)

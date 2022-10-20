import pdb
from django.shortcuts import render, redirect
from chat.models import ImageUpload, Messages, Room
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from .forms import ImageForm
from .mongo_models import *
import base64


def upload_view(request, room_name):
    """Process images uploaded by users"""
    context = {}
    data = {}
    if request.method == 'POST':
        img = request.FILES['img_name']
        img_title = request.POST['title_name']

        # read
        img_binary = fs.put(img.read(), title=img_title,
                            user_id=request.user.id, room_name=room_name, user_name = request.user.username)  # returns an object id

        # insert in table
        data['img_id'] = img_binary
        data['title'] = img_title
        data['user_id'] = request.user.id
        data['room_name'] = room_name
        # pdb.set_trace()
        obj = my_collection.insert_one(data)

        img_source = fs.get(img_binary).read()  # returns in binary format
        uploaded_at = fs.get(img_binary).upload_date

        img_url = base64.b64encode(img_source).decode()
        # pdb.set_trace()

        # save_location = os.getcwd() + "/media/images/" + img_title + "_"+ img.name
        # img_url1 = "/media/images/" + img_title + "_" + img.name

        # open and write the data
        # with open(save_location, "wb") as output:
        #     output.write(img_source)

        # to retrieve data
        # data = my_db.fs.files.find_one({'user_id': request.user.id })

        context['img_url'] = img_url
        context['uploaded_at'] = uploaded_at
        context['img_title'] = img_title

        # return render(request, 'upload.html', context)
        return redirect(f'/chat/{room_name}')
    else:
        return render(request, 'upload.html')


def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        # pdb.set_trace()
        if form.is_valid():
            form.save()
            # pdb.set_trace()
            # Get the current instance object to display in the template
            img_obj = form.instance  # it will return the image model object
            # return render(request, 'image_upload.html', {'form': form, 'img_obj': img_obj})
            return redirect('/chat/new')
    else:
        form = ImageForm()
    return render(request, 'image_upload.html', {'form': form})


def home(request):
    return render(request, 'home.html', {})


def room(request, room_name):
    context = {}
    room = Room.objects.filter(name=room_name).first()
    all_messages = []
    # all_images = []
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        if room:
            all_messages = Messages.objects.filter(room=room)
            # all_images = ImageUpload.objects.filter(room=room).order_by('-id')
        else:
            room = Room(name=room_name)
            room.save()

    # current_user = my_collection.find({'user_id':request.user.id})
    # img_id = current_user['img_id']
    # # # img = my_db.fs.files.find_one({'_id':img_id})
    # img_source = fs.get(img_id).read()
    # img_url =  base64.b64encode(img_source).decode()
    # context['img_url'] = img_url
    
    images = []
    check = fs.exists({'room_name': room_name})
    if check:
        for img in fs.find({'room_name': room_name}).sort("uploadDate", -1):
            data = {
                'room_name': img.room_name,
                'title': img.title,
                'user_id': img.user_id,
                'user_name': img.user_name,
                'url': base64.b64encode(img.read()).decode()
            }
            images.append(data)
            
    context['images'] = images
    context['room_name'] = room_name
    context['all_messages'] = all_messages
    # context['all_images'] = all_images

    return render(request, 'chatroom.html', context)


def signup_view(request):
    context = {}
    if request.user.is_authenticated:  # if the user is already authenticated
        return redirect('/chat/home')
    if request.method == 'POST':  # if user filled the form
        # passing the data's for further use
        form = UserCreationForm(request.POST)
        if form.is_valid():  # this is the function of above django's UserCreatingForm
            form.save()  # saving form for further use
            username = request.POST['username']  # entered_username
            password = request.POST['password1']  # entered_password
            # check_user = User.objects.filter(username=username).exists()
            # if not check_user: # if it's new user
            #     new_user = User.objects.create_user(username=username, password=password)
            #     new_user.save()
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('/chat/home')
        else:
            print('Form is not valid!')
            return render(request, 'signup.html', {'form': form})
    else:
        # context['form'] = UserCreationForm() # if user opening the page for first time
        print('First time opened')
        return render(request, 'signup.html', context)


def signin_view(request):
    context = {}
    # form = LoginForm()
    # context['form'] = form
    if request.user.is_authenticated:
        # return render(request, 'home.html')
        return redirect('/chat/home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/chat/home')
        else:
            # form = AuthenticationForm(request.POST)
            return render(request, 'signin.html', context)
    else:
        # form = AuthenticationForm()
        return render(request, 'signin.html', context)


def signout_view(request):
    logout(request)
    return redirect('/chat/home')


# def room(request, room_name):
#     context = {}
#     room = Room.objects.filter(name=room_name).first()
#     # images = ImageUpload.objects.filter(name=room_name).first()
#     # pdb.set_trace()
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
#     # pdb.set_trace()
#     # context['image_form'] = image_form
#     # {
#     #     'room_name': room_name,
#     #     'all_messages': all_messages,
#     #     'image_form': image_form,
#     # }
#     return render(request,'chatroom.html',context)


# def room(request, room_name):

    # if request.is_ajax and request.method == 'POST':
    #     # form = MessagesForm()
    #     # if request.method=='POST':
    #     form = MessagesForm(request.POST)
    #     if form.is_valid():
    #         instance = form.save()
    #         serialize_instance = serializers.serialize('json', [ instance ])
    #         return JsonResponse({"instance": serialize_instance}, status=200)
    #     else:
    #         # some form errors occured.
    #         return JsonResponse({"error": form.errors}, status=400)
    # return JsonResponse({"error": ""}, status=400)

    # if request.method == 'POST':
    #     # obj = Messages(message=request.POST["msg"])
    #     obj = Messages.objects.create()
    #     obj.message = request.POST.get("msg")
    #     # obj.username = request.user.username
    #     obj.username = "usernamee"
    #     obj.save()
    # return render(request, 'chatroom.html', {
    #     'room_name': room_name
    # })

    # form = MessagesForm()
    # if request.method=='POST':
    #     form = MessagesForm(request.POST)
    #     # pdb.set_trace()
    #     if form.is_valid():
    #         form.save()
    #         return redirect('home/')
    # context={
    #     'form':form,
    #     'room_name': room_name
    # }
    # return render(request,'chatroom.html',context)
    # all_users = Messages.objects.filter(date=datetime.date.today())
    # date = all_users[0].date
    # context={
    #     'all_users': all_users,
    #     'date': date,
    #     'room_name': room_name
    # }
    # return render(request,'chatroom.html',context)

from email import message
from django.shortcuts import render, redirect

from chat.models import Messages
# from chat.forms import MessagesForm


def index(request):
    return render(request, 'index.html', {})


def room(request, room_name):    
    # if request.method == 'POST':
    #     # obj = Messages(message=request.POST["msg"])
    #     obj = Messages.objects.create()
    #     obj.message = request.POST.get("msg")
    #     # obj.username = request.user.username
    #     obj.username = "usernamee"
    #     obj.save()
    return render(request, 'chatroom.html', {
        'room_name': room_name
    })


    # form = MessagesForm()
    # if request.method=='POST':
    #     form = MessagesForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         # return redirect('home/')
    # context={
    #     'form':form,
    #     'room_name': room_name
    # }
    # return render(request,'chatroom.html',context)
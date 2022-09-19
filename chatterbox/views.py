from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect

from chatterbox.models import Room, Message


# Create your views here.
def hello(request, s):
    return HttpResponse(f'Hello, {s} world!')


def home(request):
    rooms = Room.objects.all()  # najdeme všechny místnosti

    context = {'rooms': rooms}
    return render(request, 'chatterbox/home.html', context)

@login_required
def search(request, s):
    rooms = Room.objects.filter(name__contains=s)
    messages = Message.objects.filter(body__contains=s)

    context = {'rooms': rooms, 'messages': messages}
    return render(request, "chatterbox/search.html", context)

@login_required
def room(request, pk):
    room = Room.objects.get(id=pk)  # najdeme místnost se zadaným id
    messages = Message.objects.filter(room=pk)  # vybereme všechny zprávy dané místnosti

    # zpracovani nove zpravy:
    if request.method == 'POST':
        body = request.POST.get('body').strip()
        if len(body) > 0:
            message = Message.objects.create(
                user=request.user,
                room=room,
                body=body
            )
            return HttpResponseRedirect(request.path_info)

    context = {'room': room, 'messages': messages}
    return render(request, "chatterbox/room.html", context)

@login_required
def rooms(request):
    rooms = Room.objects.all()
    # messages_count = room.message_count()

    context = {'rooms': rooms} #'messages_count': messages_count}
    return render(request, "chatterbox/rooms.html", context)

'''
@login_required
def create_room(request):
    return render(request, 'chatterbox/create_room.html')
'''

@login_required
def create_room(request):
    if request.method == 'POST':
        name = request.POST.get('name').strip()
        desc = request.POST.get('desc').strip()
        if len(name) > 0 and len(desc) > 0:
            room = Room.objects.create(
                name=name,
                description=desc
            )

            return redirect('room', pk=room.id)

    return render(request, 'chatterbox/create_room.html')

'''
@login_required
def new_room(request):
    if request.method == 'POST':
        room = Room.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('descr')
        )
        return redirect('room', pk=room.id)

    return redirect('home')
'''


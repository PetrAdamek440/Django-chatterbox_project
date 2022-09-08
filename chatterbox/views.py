from django.http import HttpResponse
from django.shortcuts import render

from chatterbox.models import Room, Message

# Create your views here.
def hello(request, s):
    return HttpResponse(f'Hello {s} World!!!')

def search(request, s):
    rooms = Room.objects.filter(name__contains=s)

    messages = Message.objects.filter(body__contains=s)

    context = {'rooms': rooms, 'messages': messages}
    return render(request, 'chatterbox/search.html', context)

from django.contrib import admin

from chatterbox.models import Room, Message

# Register your models here.
admin.site.register(Room)
admin.site.register(Message)

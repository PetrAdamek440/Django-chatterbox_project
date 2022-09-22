"""chatterbox_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import chatterbox.views

from django.conf import settings  # add this
from django.conf.urls.static import static  # add this

import profiles.views

urlpatterns = [
    path('admin/', admin.site.urls),

    # chatterbox aplications:
    # path(cesta, view, name)
    path('', chatterbox.views.home, name='home'),
    path('hello/<s>', chatterbox.views.hello),

    path('search/', chatterbox.views.search, name='search'),
    #path('search/<s>', chatterbox.views.search),

    path('room/<str:pk>/', chatterbox.views.room, name="room"),
    path('rooms/', chatterbox.views.rooms, name='rooms'),

    path('create_room/', chatterbox.views.create_room, name="create_room"),
    # path('create_room/new_room', chatterbox.views.new_room, name="new_room"),

    path('delete_room/<str:pk>/', chatterbox.views.delete_room, name='delete_room'),
    path('delete_room_yes/<pk>/', chatterbox.views.delete_room_yes, name="delete_room_yes"),

    path('edit_room/<pk>', chatterbox.views.EditRoom.as_view(), name='edit_room'),

    # accounts application:
    path("accounts/", include("accounts.urls")), # sign up
    path("accounts/", include("django.contrib.auth.urls")), # ostatni

    path("__reload__/", include("django_browser_reload.urls")), # reload pro zadavani nove zpravy v room

    # profiles aplikace:
    path('users/', profiles.views.profiles_list, name='profiles'),
    path('user/<pk>', profiles.views.user_profile, name='profile'),
    path('edituser/<pk>/', profiles.views.EditProfile.as_view(), name='editprofile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # add static

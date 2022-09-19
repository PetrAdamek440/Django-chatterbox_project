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

urlpatterns = [
    path('admin/', admin.site.urls),

    # chatterbox aplications:
    # path(cesta, view, name)
    path('', chatterbox.views.home, name='home'),
    path('hello/<s>', chatterbox.views.hello),
    path('search/<s>', chatterbox.views.search),
    path('room/<str:pk>/', chatterbox.views.room, name="room"),
    path('rooms/', chatterbox.views.rooms, name='rooms'),

    path('create_room/', chatterbox.views.create_room, name="create_room"),
    # path('create_room/new_room', chatterbox.views.new_room, name="new_room"),

    # accounts application:
    path("accounts/", include("accounts.urls")), # sign up
    path("accounts/", include("django.contrib.auth.urls")), # ostatni

    path("__reload__/", include("django_browser_reload.urls")) # reload pro zadavani nove zpravy v room
]

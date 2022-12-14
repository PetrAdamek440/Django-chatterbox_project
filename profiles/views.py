

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.forms import ModelForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView

from profiles.models import Profile


@login_required
def profiles_list(request):
    #profiles = Profile.objects.all()
    allusers = User.objects.all()

    context = {'users': allusers}
    return render(request, 'profiles/users.html', context)


@login_required
def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    #user = profile.use

    context = {'profile': profile} #'user': user,
    return render(request, 'profiles/user.html', context)


class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('about_me', 'photo') # TODO editovatelne name...


class EditProfile(UpdateView):
    template_name = 'profiles/edituser.html'
    model = Profile
    form_class = EditProfileForm
    success_url = reverse_lazy('profiles')


#class CreateProfile(CreateView):
   #template_name = 'profiles/createprofile.html'
    #success_url = reverse_lazy('profiles')

@login_required
def create_profile(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name').strip()
        last_name = request.POST.get('last_name').strip()
        email = request.POST.get('email').strip()
        aboutme = request.POST.get('aboutme').strip()
        file_url = ""
        if request.FILES.get('upload'):  # pokial sme poslali subor
            upload = request.FILES['upload']  # z requestu si vytiahnem subor
            file_storage = FileSystemStorage()  # praca so suborovym systemom
            file = file_storage.save(upload.name, upload)  # ulozime subor na disk
            file_url = file_storage.url(file)

        request.user.first_name = first_name
        request.user.last_name = last_name
        request.user.email = email
        profile = Profile.objects.create(
            user=request.user,
            about_me=aboutme,
            photo=file,
        )

        return redirect('profile', pk=profile.id)

    return render(request, 'profiles/createprofile.html')





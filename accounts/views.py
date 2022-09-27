from django.contrib.auth.forms import UserCreationForm, get_user_model
from django.urls import reverse_lazy
from django.views import generic

class SignUpForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = (#"first_name","last_name",
                    "email", "username", "password1", "password2" ) # django zobrazi Password a Password confirmation:


class SignUpView(generic.CreateView):
    form_class = SignUpForm #UserCreationForm # bolo v povodnom kode
    success_url = reverse_lazy("login")
    template_name = 'accounts/signup.html'



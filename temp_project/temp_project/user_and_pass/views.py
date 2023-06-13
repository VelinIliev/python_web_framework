# from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import login, get_user_model
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from temp_project.user_and_pass.forms import SignUpForm

# from temp_project.user_and_pass.forms import SignUpForm

UserModel = get_user_model()


def index(request):
    users = UserModel.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'user_and_pass/index.html', context)


class SignUpView(views.CreateView):
    template_name = 'user_and_pass/sign-up.html'
    form_class = SignUpForm
    # success_url = '/upass/'
    success_url = reverse_lazy('index web')

    # sign-in user when registration is successful
    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


# newuser
# Pass123!
#

class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    success_url = reverse_lazy('index web')


# def sign_in(request):
#     if request.method == "GET":
#         form = SignInForm()
#     else:
#         form = SignInForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user:
#                 login(request, user)
#                 return redirect('index web')
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'user_and_pass/sign-in.html', context)

class SignInView(auth_views.LoginView):
    template_name = 'user_and_pass/sign-in.html'

    # success_url = reverse_lazy('index web')
    # redirect_field_name = 'next'

    # def get_success_url(self):
    #     if self.success_url:
    #         return self.success_url
    #
    #     return self.get_redirect_url() or self.get_default_redirect_url()


class SignOutView(auth_views.LogoutView):
    ...

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins, get_user_model

UserModel = get_user_model()


# @login_required
# def index(request):
#     users = User.objects.all()
#     context = {
#         'users': users,
#     }
#     return render(request, 'user_and_pass/index.html', context)

# class UsersListView(LoginRequiredMixin, views.ListView):
#     model = User
#     template_name = 'user_and_pass/index.html'
#     context_object_name = 'users'

class UsersListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = UserModel
    template_name = 'user_and_pass/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(self.request.user.__class__)
        # users = UserModel.objects.all()
        return context

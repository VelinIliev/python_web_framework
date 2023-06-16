from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins, get_user_model

from temp_project.web.models import TestProfile
from django.contrib.auth import mixins as auth_mixins

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


class TestView(views.ListView):
    template_name = 'tests/index.html'
    model = TestProfile

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['profiles_count'] = self.object_list.count()
        # context['username'] = self.request.user.email or 'anonymous'
        context['query'] = self.request.GET.get('query')
        return context


class ProfileCreateView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model = TestProfile
    fields = '__all__'
    template_name = 'tests/create.html'
    success_url = reverse_lazy('test view')

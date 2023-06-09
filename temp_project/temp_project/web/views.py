from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic as views


# @login_required
# def index(request):
#     users = User.objects.all()
#     context = {
#         'users': users,
#     }
#     return render(request, 'user_and_pass/index.html', context)

class UsersListView(LoginRequiredMixin, views.ListView):
    model = User
    template_name = 'user_and_pass/index.html'
    context_object_name = 'users'

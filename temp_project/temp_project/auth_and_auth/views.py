from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views import generic as views
from django.contrib.auth import mixins
from django.shortcuts import render

from django.contrib.auth.models import User

from temp_project.auth_and_auth.custom_decorator import allow_groups


def index(request):
    print(request.user)
    user_message = '' if request.user.is_authenticated else 'not '
    return HttpResponse(f'The user is {user_message}authenticated')


def create_new_user(request):
    new_user = User.objects.create_user(
        username="donchominkov2",
        password="d0n40minK0v",
        first_name="Doncho",
        last_name="Minkov",
    )
    return HttpResponse(f'Created!')


# 1. createsuperuser via terminal
# 2. create user via admin panel

# doncho
# Minkov02!

# 3. create user with code: User.objects.create_user() or User.objects.create_superuser()

def authenticated_user(request):
    print(authenticate(username='doncho', password='Minkov02!'))
    return HttpResponse("OK")


def create_user_and_login(request):
    print(request.user)
    user = User.objects.create_user(
        username='Pesho',
        password='Minkov02!',
    )
    login(request, user)
    print(request.user)
    return HttpResponse("OK")


def check_permissions(request):
    usernames = ('Pesho', 'doncho', 'velko')

    users = User.objects.filter(username__in=usernames)

    permissions_to_check = ['auth.add_user', 'auth.change_user', 'auth.delete_user', 'auth.view_user']

    print(users)

    for user in users:
        print('*' * 30)
        print(user)
        for perm in permissions_to_check:
            print(f'{perm.split(".")[1]}: {user.has_perm(perm)}')
    print('*' * 30)

    return HttpResponse("OK")


# @login_required(login_url='/login/')
# по-добре в settings.py
@login_required()
def show_profile(request):
    return HttpResponse(request.user.username)


# login required
class ProfileView(mixins.LoginRequiredMixin, views.View):
    def get(self, request):
        return HttpResponse(request.user)


@allow_groups(groups=['test'])
# @allow_groups
def decorated_func(request):
    return HttpResponse(f'OK')
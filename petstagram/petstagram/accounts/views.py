from django.contrib.auth import views as auth_views, get_user_model
from django.urls import reverse_lazy
from django.views import generic as views
from django.http import HttpResponse
from django.shortcuts import render

from petstagram.accounts.forms import UserCreateForm
from petstagram.photos.models import Photo

UserModel = get_user_model()


# def login_user(request):
#     return render(request, template_name='accounts/login-page.html')

class SignInView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'


# def register_user(request):
#     return render(request, template_name='accounts/register-page.html')

class SignUpView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = UserCreateForm
    # fields = ('username', 'email', 'password1', 'password2')
    success_url = reverse_lazy('index')


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


# def show_user_details(request, pk):
#     return render(request, template_name='accounts/profile-details-page.html')

class UserDetailsView(views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        context['pets_count'] = self.object.pet_set.count()

        photos = self.object.photo_set.prefetch_related('like_set')

        # Photo.objects.select_related()

        context['photos_count'] = photos.count()
        context['likes_count'] = sum(x.like_set.count() for x in photos)
        return context


# def edit_user(request, pk):
#     return render(request, template_name='accounts/profile-edit-page.html')
class EditUserView(views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'gender', 'email')

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={'pk': self.request.user.pk, })


# def delete_user(request, pk):
#     return render(request, template_name='accounts/profile-delete-page.html')

class DeleteUserView(views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')

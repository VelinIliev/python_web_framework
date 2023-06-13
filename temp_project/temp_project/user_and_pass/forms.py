from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms

from temp_project.user_and_pass.models import Profile

UserModel = get_user_model()
#
#
# class AppUserCreationForm(auth_forms.UserCreationForm):
#     class Meta:
#         model = UserModel
#         fields = (UserModel.USERNAME_FIELD, 'password1', 'password2',)
#         field_classes = {'username': auth_forms.UsernameField}


class SignUpForm(auth_forms.UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField()

    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password1', 'password2', 'first_name', 'last_name', 'age')
        field_classes = {'username': auth_forms.UsernameField}

    def save(self, commit=True):
        user = super().save(commit=commit)
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        age = self.cleaned_data['age']
        profile = Profile(
            first_name=first_name,
            last_name=last_name,
            age=age,
            user=user,
        )
        if commit:
            profile.save()

        return user

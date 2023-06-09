from django.contrib.auth.views import LoginView
from django.urls import path, include

from temp_project.user_and_pass.views import index, SignUpView, SignInView, SignOutView

urlpatterns = [
    # path('', index, name='user and pass index'),
    path('signup/', SignUpView.as_view(), name='sign up'),
    # path('sign-in/', sign_in, name='sign in'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('logout/', SignOutView.as_view(), name='logout'),
]

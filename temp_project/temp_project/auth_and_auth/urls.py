from django.urls import path, include

from temp_project.auth_and_auth.views import index, create_new_user, authenticated_user, create_user_and_login, \
    check_permissions, show_profile, ProfileView, decorated_func

urlpatterns = [
    path('', index, name='index auth'),
    path('user/', create_new_user, name='create user'),
    path('auth/', authenticated_user, name='auth user'),
    path('login/', create_user_and_login, name='create and login user'),
    path('check/', check_permissions, name='check permissions'),
    path('show/', show_profile, name='show profile'),
    path('show2/', ProfileView.as_view(), name='show profile2'),
    path('deco/', decorated_func, name='decorator'),
]

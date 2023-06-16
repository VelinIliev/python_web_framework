from django.urls import path, include

from temp_project.web.views import UsersListView, TestView, ProfileCreateView

urlpatterns = [
    path('', UsersListView.as_view(), name='index web'),
    path('testview/', TestView.as_view(), name='test view'),
    path('create/', ProfileCreateView.as_view(), name='test profile create'),
]

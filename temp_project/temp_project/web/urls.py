from django.urls import path, include

from temp_project.web.views import UsersListView

urlpatterns = [
    path('', UsersListView.as_view(), name='index web'),

]

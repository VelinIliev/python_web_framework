from django.urls import path, include

from temp_project.web_tools.views import index, clicks_counter, EmployeesListViews
from .signals import *

urlpatterns = [
    path('', index, name='index tools'),
    path('count/', clicks_counter, name='click tools'),
    path('list/', EmployeesListViews.as_view(), name='paginator tools'),
]

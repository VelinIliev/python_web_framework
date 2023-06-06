from django.urls import path
from django.views import generic as views

from temp_project.class_based_views.views import index, IndexView, IndexViewWithTemplate, IndexViewWithListView, \
    EmployeeDetailsView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView

urlpatterns = [
    # path('', index),
    path('', IndexView.as_view(), name='index'),
    path('template/', IndexViewWithTemplate.as_view(), name='template view'),
    path('redirect-to-index/', views.RedirectView.as_view(url="/cbv/"), name='redirect to index'),
    path('list/', IndexViewWithListView.as_view(), name='list view'),
    path('details/<int:pk>/', EmployeeDetailsView.as_view(), name='employee details'),
    path('create/', EmployeeCreateView.as_view(), name='employee create'),
    path('update/<int:pk>', EmployeeUpdateView.as_view(), name='employee update'),
    path('delete/<int:pk>', EmployeeDeleteView.as_view(), name='employee delete'),
]

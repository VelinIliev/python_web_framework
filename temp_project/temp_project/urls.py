from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cbv/', include('temp_project.class_based_views.urls')),
]

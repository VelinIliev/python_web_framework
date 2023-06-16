from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cbv/', include('temp_project.class_based_views.urls')),
    path('auth/', include('temp_project.auth_and_auth.urls')),
    path('upass/', include('temp_project.user_and_pass.urls')),
    path('web/', include('temp_project.web.urls')),
    path('tools/', include('temp_project.web_tools.urls')),
    # path('tests/', include('temp_project.tests.urls')),
]

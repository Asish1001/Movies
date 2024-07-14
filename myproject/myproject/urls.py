from django.contrib import admin
from django.urls import path, include
from movies.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Add this line for the root URL
    path('api/', include('movies.urls')),
]

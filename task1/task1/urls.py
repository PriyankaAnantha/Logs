from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('task1app.urls')),  # Route the root URL to task1app's URLs
]
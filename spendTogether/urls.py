from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),  # Register, login, logout endpoints
    path('auth/token/', include('djoser.urls.authtoken')),  # Token-based auth
]

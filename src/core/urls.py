from barberq import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # Endpoint for account management (login, logout, etc.)
    path('accounts/', include('django.contrib.auth.urls')),
    # Index page (landing page) for the app
    path('', views.home, name='home'),
    # Endpoint for the reservation page, allows clients to make reservations
    path('reservations/', views.reservation, name='reservation'),
]

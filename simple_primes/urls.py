from django.contrib import admin
from django.urls import path
from primes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.input_page, name='home'),
    path('primes/', views.output_page, name='primes'),
]



from django.contrib import admin
from django.urls import path
from enroll.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
]

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('clinical/', include('clinical.urls'), name='clinical'),
    path('accounts/', include('accounts.urls'), name='accounts'),
]

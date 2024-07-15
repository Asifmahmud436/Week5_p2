from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='homepage'),
    path('author/', include('author.urls')),
    path('album/', include('album.urls')),
]

from django.urls import path,include
from .import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('add/',views.AddAuthorView.as_view(),name='add_author'),
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('edit/<int:id>',views.EditAuthorView.as_view(),name='edit_author'),
]

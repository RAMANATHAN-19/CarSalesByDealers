from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="login"),
    path('dashboard', views.listing, name="listing"),
    path('forgot', views.forgot, name="forgot"),
    path('logout', views.logout, name="logout"),
    path('changepassword', views.changepassword, name="changepassword"),
]


"""car_sales_service_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from api.views import ListUsers, CustomAuthToken
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', include('pages.urls')),
    path('api/users/',ListUsers.as_view()),
    path('api/token/auth/', CustomAuthToken.as_view()),
    path('api-token-auth', obtain_auth_token,name='api_token_auth'),
    path('pages/', include('pages.urls')),
    path('product/', include('product.urls')),
    path('sales/', include('sales.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
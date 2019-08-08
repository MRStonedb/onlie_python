"""online_python URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from backend.views import CodeViewSet, RunCodeAPIView, home, js, css

router = DefaultRouter()
router.register(prefix='code', viewset=CodeViewSet, base_name='code')

API_V1 = [url(r'^run/$', RunCodeAPIView.as_view(), name='run')]

API_V1.extend(router.urls)

API_VERSIONS = [url(r'^v1/', include(API_V1))]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(API_VERSIONS)),
    url(r'^js/(?P<filename>.*\.js)$', js, name='js'),
    url(r'^css/(?P<filename>.*\.css)$', css, name='css'),
    url(r'^$', home, name='home')
]
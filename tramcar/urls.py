"""tramcar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from job_board.forms import CssAuthenticationForm

admin.site.site_header = "YMI Job Board Administration"
admin.site.site_title = "YMI Job Board Administration"
admin.site.index_title = "YMI Job Board Administration"

urlpatterns = [
    url(r'^', include('job_board.urls')),
    url(r'^admin/', admin.site.urls),
    # url('^', include('django.contrib.auth.urls')),
    url(
        r'^login/$',
        auth_views.LoginView.as_view(
            authentication_form=CssAuthenticationForm,
            extra_context={'title': 'Login'}
        ),
        name='login'
    ),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
]

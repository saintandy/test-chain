"""test-chain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en//topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
import establishment.chat.views

urlpatterns = [
    url(r'^djangoadmin/', admin.site.urls),
    url(r"^", include("establishment.localization.urls")),
    url(r"^", include("establishment.content.urls_single_page")),
    url(r"^accounts/", include("establishment.accounts.urls_single_page")),

    url(r"^blog/", include("establishment.blog.urls_single_page")),
    url(r"^forum/", include("establishment.forum.urls_single_page")),
    url(r"^docs/", include("establishment.documentation.urls")),
    url(r"^chat/", include("establishment.chat.urls")),

    url(r"^messages/", establishment.chat.views.private_chat),
    # url(r"^email/", include("establishment.emailing.urls")),
    url(r"^baseconfig/", include("establishment.baseconfig.urls")),

    # Your own urls
    url(r"^", include("test-chainapp.urls")),
]

if settings.DEBUG:
    # Alter the function that serves static files, to wait for bundling to be ready

    from django.views import static as static_view

    old_staticfiles_serve = static_view.serve

    def static_serve(request, static_path, document_root=None, **kwargs):
        print("Going to serve a static file:", static_path, document_root, kwargs)
        return old_staticfiles_serve(request, static_path, document_root=document_root, **kwargs)

    static_view.serve = static_serve
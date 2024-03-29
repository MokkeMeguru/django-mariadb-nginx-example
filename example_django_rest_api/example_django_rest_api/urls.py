"""example_django_rest_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import routers
from ping_pong import views

from draft_todo import views as dview
import rest_auth

schema_view = get_schema_view(
    openapi.Info(
        title="Restful API Lists",
        default_version='v1',
        description="Django Rest Framework Swagger : First Steps",
        terms_of_service="https://github.com/MokkeMeguru",
        contact=openapi.Contact(email="meguru.mokke@gmail.com"),
        license=openapi.License(name="MIT"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)
router = routers.DefaultRouter()
router.register(r'authuser', dview.TaskAuthUserAPIView)

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
    url(r'^redoc/$',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),
    url(r'^redoc/$',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),
    url(r'ping', views.PingPongView.as_view(), name='ping'),
    url(r'draft_user/create_user',
        dview.TaskUserCreateAPIView.as_view(),
        name='dcu'),
    url(r'draft_user/create_task',
        dview.TaskTodoItemCreateAPIView.as_view(),
        name='dct'),
    path(r'draft_user/list_task/<str:owner>',
        dview.TaskTodoItemListAPIView.as_view(),
        name='dlt'),
    path('draft_user/retrieve_task/<int:pk>',
        dview.TaskTodoItemRetrieveAPIView.as_view(),
        name='drt'),
    path('draft_user/authuser/',
         include(router.urls),
        name='da'),
    path('draft_authuser/create_task',
         dview.TaskAuthUserCreateTodoItemAPIView.as_view(),
        name='dact'),
    path('rest-auth/', include('rest_auth.urls')),
    path('accounts/login/', dview.not_authorized)
]

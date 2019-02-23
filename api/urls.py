"""paranuara URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from rest_framework.schemas import get_schema_view

# Create a router and register viewsets with it.
router = DefaultRouter()
router.register(r'fruits_and_vegetables',
                views.FruitsAndVegetablesViewset,
                basename='fruits_and_vegetables')
router.register(r'employees',
                views.CompanyEmployeesViewset,
                basename='employees')

schema_view = get_schema_view(
    title='A Paranuara API',
    renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer]
)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/twopeople/<int:pk1>/<int:pk2>/', views.TwoPeopleView.as_view(), name='twopeople'),
    path('', schema_view, name="docs"),
]

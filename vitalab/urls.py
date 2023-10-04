from django.contrib import admin
from django.urls import include, path

urlpatterns: list = [
    path(route='admin/', view=admin.site.urls),
    path(route='usuarios/', view=include(arg='usuarios.urls')),
]

from django.urls import path
from usuarios import views

urlpatterns: list = [
    path(route='cadastro/', view=views.cadastro, name='cadastro'),
]

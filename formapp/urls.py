from django.urls import path
from .import views

urlpatterns=[
    path('',views.indexproduct),
    path('add',views.addproduct)
]
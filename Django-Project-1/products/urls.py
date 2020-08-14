from django.urls import path
from . import views

# /products/1/detail 
# /products/new
# don't call function django will take care at run time when the request is made

urlpatterns = [
    path('',views.index),
    path('prod',views.prod)
]
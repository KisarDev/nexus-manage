from django.urls import path
# now import the views.py file into this code
from . import views
urlpatterns = [
    path('get_acess_token', views.get_acess_token, name="get_acess_token"),
    path('page_redirect', views.page_redirect, name="page-redirect"),
    path('user', views.mercado_livre_user, name="mercado_livre_user"),
]

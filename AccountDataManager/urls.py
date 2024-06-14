from django.urls import path

from . import views

urlpatterns = [
    path(route="CreateAccount/", view=views.SaveLoginInfo),
    path(route="changePassword/<int:pk>/", view=views.changePassword),
    path(route="allusers/", view=views.getusers)

]
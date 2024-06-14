from django.urls import path

from . import views

urlpatterns = [
    path(route="accountdetailes/", view=views.saveUserInformation),
    path(route="updateprofile/", view=views.updateInformation),
    path(route="delete/", view=views.deleteUser)
]
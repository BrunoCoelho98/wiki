from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("new", views.new_page, name="new_page"),
    path("edit", views.edit, name="edit"),
    path("saveEdit", views.saveEdit, name="saveEdit"),
    path("rand", views.rand, name="rand")
]

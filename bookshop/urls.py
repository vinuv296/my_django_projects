from django.urls import path

from bookshop.views import create_book
urlpatterns=[
    path("book",create_book,name="createbook")



]
from django.shortcuts import render, redirect
from bookshop.forms import CreateBookForm
from .models import Book


# Create your views here.

def create_book(request):
    form =CreateBookForm()
    context={}
    context["form"]=form
    if request.method == "POST":
        form=CreateBookForm(request.POST,files=request.FILES)
        if form.is_valid:
            form.save()
            return render(request,"book_add.html",context)

    return render(request, "book_add.html", context)


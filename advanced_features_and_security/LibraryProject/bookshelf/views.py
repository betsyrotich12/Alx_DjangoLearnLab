from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import csrf_exempt
from .models import Book
from django import forms

# Define a form for handling book title updates
class BookEditForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title']

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()  # Retrieve all books
        return render(request, 'bookshelf/book_list.html', {'books': books})
    return HttpResponse(status=405)  # Method Not Allowed

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        form = BookEditForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204)  # No Content
        else:
            return HttpResponse(status=400)  # Bad Request
    else:
        form = BookEditForm(instance=book)
        return render(request, 'bookshelf/edit_book.html', {'form': form})

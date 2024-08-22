from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book

# Create your views here.


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    return HttpResponse(status=204)  # No Content

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        new_title = request.POST.get('title', book.title)
        book.title = new_title
        book.save()
        return HttpResponse(status=204)  # No Content
    else:
        return HttpResponse(status=204)  # No Content

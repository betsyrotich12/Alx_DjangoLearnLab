from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookSearchForm
from .forms import BookEditForm

# View to handle book listing with search functionality
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    if request.method == 'GET':
        form = BookSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            books = Book.objects.filter(title__icontains=query)
        else:
            books = Book.objects.all()
        return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})
    return HttpResponse(status=405)  # Method Not Allowed

# View to handle book editing
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

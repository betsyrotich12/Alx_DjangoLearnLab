# from django.shortcuts import render, get_object_or_404, redirect
# from django.views.generic.detail import DetailView
# from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.views import LoginView, LogoutView
# from django.contrib.auth.decorators import user_passes_test
# from django.contrib.auth.decorators import permission_required
# from .models import Book 
# from .models import Library


# # View to list all books
# def list_books(request):
#     books = Book.objects.all()
#     return render(request, 'relationship_app/list_books.html', {'books': books})

# # Detail view for a specific library
# class LibraryDetailView(DetailView):
#     model = Library
#     template_name = 'relationship_app/library_detail.html'
#     context_object_name = 'library'

# # User registration view
# def register(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)  # Automatically log in the user after registration
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'relationship_app/register.html', {'form': form})

# # Custom login view
# class CustomLoginView(LoginView):
#     template_name = 'relationship_app/login.html'

# # Custom logout view
# class CustomLogoutView(LogoutView):
#     template_name = 'relationship_app/logout.html'

# # Role-based access control functions
# def is_admin(user):
#     return user.userprofile.role == 'Admin'

# def is_librarian(user):
#     return user.userprofile.role == 'Librarian'

# def is_member(user):
#     return user.userprofile.role == 'Member'

# # Views restricted by user roles
# @user_passes_test(is_admin)
# def admin_view(request):
#     return render(request, 'relationship_app/admin_view.html')

# @user_passes_test(is_librarian)
# def librarian_view(request):
#     return render(request, 'relationship_app/librarian_view.html')

# @user_passes_test(is_member)
# def member_view(request):
#     return render(request, 'relationship_app/member_view.html')

# # Views restricted by custom permissions on the Book model
# @permission_required('relationship_app.can_add_book', raise_exception=True)
# def add_book(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         author_id = request.POST.get('author')
#         if title and author_id:
#             Book.objects.create(title=title, author_id=author_id)
#             return redirect('list_books')
#     return render(request, 'relationship_app/add_book.html')

# @permission_required('relationship_app.can_change_book', raise_exception=True)
# def edit_book(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         author_id = request.POST.get('author')
#         if title and author_id:
#             book.title = title
#             book.author_id = author_id
#             book.save()
#             return redirect('list_books')
#     return render(request, 'relationship_app/edit_book.html', {'book': book})

# @permission_required('relationship_app.can_delete_book', raise_exception=True)
# def delete_book(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'POST':
#         book.delete()
#         return redirect('list_books')
#     return render(request, 'relationship_app/delete_book.html', {'book': book})

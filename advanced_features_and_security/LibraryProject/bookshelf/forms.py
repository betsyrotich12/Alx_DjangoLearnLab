from django import forms
from .models import Book

# Form for searching books by title
class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label='Search by Title')

# Form for editing a book's title
class BookEditForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title']
        labels = {
            'title': 'Book Title',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter new title'}),
        }

# Example form to demonstrate form structure
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(widget=forms.Textarea, label='Your Message')

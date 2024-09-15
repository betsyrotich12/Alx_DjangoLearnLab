from django import forms
from .models import Profile
from .models import Post
from .models import Comment
from taggit.forms import TagWidget

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']

class PostForm(forms.ModelForm):
    #  tags = forms.ModelMultipleChoiceField(
    #     queryset=Tag.objects.all(),
    #     widget=forms.CheckboxSelectMultiple
    # )
     class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'tags': TagWidget(),  # Use TagWidget for tags field
        }
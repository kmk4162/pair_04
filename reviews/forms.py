from .models import Comment, Review
from django import forms

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['movie_name', 'title', 'content', 'grade', ]


from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
    
    # prevent user editing email
    # def __init__(self, *args, **kwargs):
    #     super(CommentForm, self).__init__(*args, **kwargs)
    #     self.fields['name'].disabled = True
    # def __init__(self, *args, **kwargs):
    #     super(CommentForm, self).__init__(*args, **kwargs)
    #     self.fields['email'].disabled = True



class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'slug', 'samplebody', 'body', 'categories','image', 'status')
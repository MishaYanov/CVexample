from django import forms
from blog.models import Post, Comment


class PostForm(forms.ModelForm):
            
    class Meta:
        model = Post
        fields = ("author","title", "text", 'link','tags', 'short_description')
        
    widget = {
        'title':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.Textarea(attrs={'class':'editable post_fields medium-editor-textarea postcontent'}),
        'short_description':forms.TextInput(attrs={'width':'200','height':'48'})

    }

class CommentForm(forms.ModelForm):
    
    
    class Meta:
        model = Comment
        fields = ("author", "text")
        
        widgets = {
            'author':forms.TextInput(attrs={'class':'commentclass'}),
            'text':forms.Textarea(attrs={'class':'editable comment_fields medium-editor-textarea commentcontnet'})
        }
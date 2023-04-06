from django import forms
from comment_app.models import Comment


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['date_sent', 'status', 'article']

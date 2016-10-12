from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')

# 创建用户添加评论的表格


class CommentForm(forms.ModelForm):
    """docstring for CommentForm"""
    class Meta:
        model = Comment
        fields = ('author', 'text',)

from django import forms
from .models import *



class CommentForm(forms.ModelForm):


    class Meta:
        model = Comments
        fields = ['which_post', 'name', 'email', 'subject', 'message']


class ReplayForm(forms.ModelForm):


    class Meta:
        model = Replay
        fields = ['which_comment', 'message']


class PostForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = ['title', 'content1', 'content2', 'content3', 'content4', 'content5', 'endcontent', 'banner', 'topic1', 'topic2', 'counted_views', 'counted_comment', 'status', 'image', 'second_image', 'author', 'auther_img', 'auther_bio', 'twitter', 'facebook', 'instagram', 'category', 'tag', 'published_date']
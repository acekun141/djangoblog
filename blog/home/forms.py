from django import forms
from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = ['title','content','image']
		widgets = {
			'title': forms.widgets.TextInput(attrs={
					'class':'form-control'
				}),
			'content': forms.Textarea(attrs={
					'class':'form-control',
				}),
		}
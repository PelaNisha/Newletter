from django import forms
from . models import post

class PostForm(foms.Modelform):
    class Meta:
        model = post
        fields = ('title','body')

        widgets = {
            'title' : forms.TextInput()
            'body': forms.Textarea()
        }
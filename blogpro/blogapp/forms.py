from django import forms
from blogapp.models import Comment

class Emailshare(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False,widget=forms.Textarea)

class commentform(forms.ModelForm):
    class Meta :
        model=Comment
        fields=('name','email','body')

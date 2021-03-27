from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ["username","email","password1","password2"]:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({'class' : 'form-control'})
    class Meta:
        model = User
        fields = ("username","email","password1","password2")
    
    def save(self, commit=True): 
        user = super(MyUserCreationForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
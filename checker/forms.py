from django import forms

class PasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password here'}), max_length=200) 
    ## 'PasswordInput' defies that the entered password will be hidden and will be shown as dots

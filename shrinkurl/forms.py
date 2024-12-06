from django import forms

class LongURLForm(forms.Form):
    longurl = forms.CharField(widget=forms.TextInput(attrs={'class': 'form', 'placeholder' : 'Enter URL to shorten here', 'size': '40'}), label="")
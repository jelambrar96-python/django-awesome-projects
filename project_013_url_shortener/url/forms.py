# url/forms.py
from django import forms

class Url(forms.Form):
    url = forms.CharField(label="URL")  # Input field for the original URL

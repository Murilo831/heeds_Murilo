from django import forms
from .models import Search


class SearchForm(forms.ModelForm):
    address = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Enter the address'}))

    class Meta:
        model = Search
        fields = ['address']

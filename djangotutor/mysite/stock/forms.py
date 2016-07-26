from django import forms
import datetime

class NameForm(forms.Form):
    your_name = forms.CharField(label='Stock Symbol:', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'DATA'}))
    start_date = forms.DateTimeField(label='Analysis Start Date:', widget=forms.TextInput(attrs={'placeholder': '2016-06-01'}))
    your_name2 = forms.CharField(label='Stock Symbol:', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'AAPL'}))
    start_date2 = forms.DateTimeField(label='Analysis Start Date:', widget=forms.TextInput(attrs={'placeholder': '2016-06-01'}))
    
    
#class NameForm(forms.Form):
#   your_name = forms.CharField(label='Your name', max_length=100)
# tank = forms.IntegerField(widget=forms.HiddenInput(), initial=123)
#http://localhost:8888/edit/djangotutor/mysite/stock/forms.py#

#class NameForm(forms.Form):
#   your_name = forms.CharField(label='Stock Symbol:', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'DATA'}))
#  start_date = forms.DateTimeField(label='Analysis Start Date:', widget=forms.TextInput(attrs={'placeholder': '2016-06-01'}))
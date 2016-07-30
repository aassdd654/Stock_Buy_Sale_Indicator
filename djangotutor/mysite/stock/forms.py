from django import forms
from .models import Stock
import datetime
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget
#See more at: http://django-datetime-widget.asaglimbeni.me/model_form_v2/#sthash.FuAOMeU1.dpuf
# https://github.com/asaglimbeni/django-datetime-widget

#from bootstrap3_datepicker.fields import DatePickerField
from bootstrap3_datepicker.widgets import DatePickerInput

#STOCKS = (("Stock Symbol", "Stock Comany Name"))
STOCKS = (('', 'Select Stock'),
          ('DATA', 'Tableau'),
          ('AAPL', 'Apple Inc'),
          ('DIS', 'Disney'),
          ('GILD', 'Gilead Science'),
        )


class NameForm(forms.Form):
    #worked:
    auto_id = False
    your_name1 = forms.CharField(label="Stock Symbol",
                                 max_length=25,
                                 widget=forms.Select(choices=STOCKS,
                                                    ),
                                 )
    your_name2 = forms.CharField(max_length=25,
                                 label="",
                                 widget=forms.Select(choices=STOCKS,
                                                    ),
                                 )
    your_name3 = forms.CharField(max_length=25,
                                 label="",
                                 widget=forms.Select(choices=STOCKS,
                                                    ),
                                 )
    your_name4 = forms.CharField(max_length=25,
                                 label="",
                                 widget=forms.Select(choices=STOCKS,
                                                    ),
                                 )
    
    start_date = forms.DateField(label='Analysis Start Date:',
                                 widget=DateWidget(usel10n=True, bootstrap_version=2),
                                 initial="2016-06-01",
                                )


# Field.choices
# An iterable (e.g., a list or tuple) consisting itself of iterables of exactly two items (e.g. [(A, B), (A, B) ...]) to use as choices for this field. If this is given, the default form widget will be a select box with these choices instead of the standard text field. The first element in each tuple is the actual value to be stored, and the second element is the human-readable name.





# worked:
    
    
#class NameForm(forms.Form):
#    your_name1 = forms.CharField(label='Stock Symbol:', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Stock 1'}))
#    start_date1 = forms.DateField(label='Analysis Start Date:',
#                                widget=DateWidget(usel10n=True, bootstrap_version=2),
#                               initial="2016-06-01")
    
    
    
#    your_name2 = forms.CharField(label='Stock Symbol:', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Stock 2'}))
#    start_date2 = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=2))
#    your_name3 = forms.CharField(label='Stock Symbol:', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Stock 3'}))
#    start_date3 = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=2))
#    your_name4 = forms.CharField(label='Stock Symbol:', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Stock 4'}))
# start_date4 = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=2))
    
    
    
######################################below is previous version#########################################################
    
    #worked:
    #start_date = forms.DateField(label='Analysis Start Date:', 
    #                             input_formats=["%Y-%m-%d"],
    #                            widget=DatePickerInput(format="%Y-%m-%d",
    #                                                     attrs={'placeholder': '2016-06-01'},
    #                                                     options={"minViewMode": "months"}))
        
#class NameForm(forms.Form):
    #your_name = forms.CharField(label='Stock Symbol:', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'DATA'}))
    #worked:
    #start_date = forms.DateTimeField(label='Analysis Start Date:', widget=forms.TextInput(attrs={'placeholder': '2016-06-01'}))
    #test:
    #start_date = forms.DateTimeField(widget=SplitSelectDateTimeWidget(hour_step=2, minute_step=15, second_step=30, twelve_hr=True, years=[2008,2009,2010], attrs={'placeholder': '2016-06-01'}))
    
    #worked.
    #your_name2 = forms.CharField(label='Stock Symbol:', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'AAPL'}))
    #start_date2 = forms.DateTimeField(label='Analysis Start Date:', widget=forms.TextInput(attrs={'placeholder': '2016-06-01'}))
    #your_name3 = forms.CharField(label='Stock Symbol:', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'GILD'}))
    #start_date3 = forms.DateTimeField(label='Analysis Start Date:', widget=forms.TextInput(attrs={'placeholder': '2016-06-01'}))
    #your_name4 = forms.CharField(label='Stock Symbol:', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'DIS'}))
    #start_date4 = forms.DateTimeField(label='Analysis Start Date:', widget=forms.TextInput(attrs={'placeholder': '2016-06-01'}))

    
    
#class NameForm(forms.Form):
#   your_name = forms.CharField(label='Stock Symbol:', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'DATA'}))
#  start_date = forms.DateTimeField(label='Analysis Start Date:', widget=forms.TextInput(attrs={'placeholder': '2016-06-01'}))
from django import forms
from .models import Stock
import datetime
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget
#See more at: http://django-datetime-widget.asaglimbeni.me/model_form_v2/#sthash.FuAOMeU1.dpuf
# https://github.com/asaglimbeni/django-datetime-widget

#from bootstrap3_datepicker.fields import DatePickerField
from bootstrap3_datepicker.widgets import DatePickerInput

#STOCKS = (("Stock Symbol", "Stock Comany Name"))

####################################################################################################

# get the stocks list from CSV. 


from cs103 import *
from collections import namedtuple
import matplotlib.pyplot as pyplot
import matplotlib.dates as dates
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from django.core.files import File

###############################

# Use WIKI-datasets-codes.csv to test



# Source Data sample
# 0     1    
"""
WIKI/AAPL	Apple Inc (AAPL) Prices, Dividends, Splits and Trading Volume
WIKI/BXP	Boston Properties Inc. (BXP) Prices, Dividends, Splits and Trading Volume
WIKI/CMA	Comerica Inc. (CMA) Prices, Dividends, Splits and Trading Volume
WIKI/COF	Capital One Financial Corp (COF) Prices, Dividends, Splits and Trading Volume
WIKI/CSX	CSX Corp (CSX) Prices, Dividends, Splits and Trading Volume
WIKI/CTSH	Cognizant Technology Solutions Corp. (CTSH) Prices, Dividends, Splits and Trading Volume
WIKI/DFS	Discover Financial Services (DFS) Prices, Dividends, Splits and Trading Volume
"""


################################

# Data Definition - Stock's ID

Stockid = namedtuple("Stockid", ["stockid", "companyname"])
# Stockid = (str, str)
# Stockid is the stock information including id and company name

# Example:
S0 = Stockid('', 'Select Stock')
S1 = Stockid("WIKI/AAPL", "Apple Inc (AAPL) Prices, Dividends, Splits and Trading Volume")
S2 = Stockid("WIKI/DATA", "Tableau Software (DATA) Prices, Dividends, Splits and Trading Volume")


# Template:
'''
def fn_for_Dailytrading(t):
        return Dailytrading.date
'''

#################################

#Target data example:
#STOCKS = (("Stock Symbol", "Stock Comany Name"))

"""
stockids = (('', 'Select Stock'),
          ('DATA', 'Tableau'),
          ('AAPL', 'Apple Inc'),
        )
"""

# Data Definition - Stock List

#L1 = [S0, S1, S2...Sn]

# Template:
'''
def fn_for_lop(periods):
    # acc is ...
    acc = ...
    for s in los:
        ... s acc
    return acc
'''

#################################
# Function: READ From File: 


def make_stockids(lines):
    """
    [str, str] 
    # template to return Stockid
    """
    # "stockid", "companyname"
    # ('WIKI/FURX', '"Furiex Pharmaceuticals')
    # convert from 'WIKI/FURX' to FURX
    
    stockid = str(lines[0])[5:]
    
    # convert the compnay name
    companyname = str(lines[1])[:]
    
    return (stockid, companyname)


 
def read(file):
    '''
    # str -> [Dailytrading]
    # convert the file to a list of Dailytrading
    '''
    # f = open('/path/to/hello.world', 'w')
    f = open(file, 'r')
    # moves past the first line
    #file_readline(f)
    # stockids is [Stockid]
    stockids = []
    # lines is a list of (the list of 2 attributes: "id", "companyname")
    line = []
    count = 0
    
    for line in f:
        # [S1, ...Sn]
        stockids = stockids + [make_stockids(line.split(","))]
    return stockids

STOCKIDS = read('/Users/chuli/Stock_Buy_Sale_Indicator/djangotutor/mysite/stock/WIKI-datasets-codes.csv')


#########################################################################################

STOCKS = [('', 'Select Stock'),
          ('DATA', 'Tableau'),
          ('AAPL', 'Apple Inc'),
          ('DIS', 'Disney'),
          ('GILD', 'Gilead Science'),
          ('TSLA', 'Tesla Motors'),
          ('ILMN', 'Illumina'),
          ('HD', 'Home Depot'),
          ('AMZN', 'Amazon'),
          ('IRBT', 'iRobot'),
          ('EL', 'Estee Lauder'),
          ('GOOG', 'Google'),
        ]



###########################################################################
class NameForm(forms.Form):
    #worked: checks
    #stocklist = forms.CharField(label="Stock Symbol",
                   #              max_length=25, widget=forms.CheckboxSelectMultiple(choices=STOCKIDS,
                                                 #   ),
                                 #)
    
    #Worked
    stocklist = forms.CharField(label="Stock Symbol",
                                max_length=25,
                                widget=forms.Select(choices=STOCKIDS,
                                                    ),
                              )
    
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
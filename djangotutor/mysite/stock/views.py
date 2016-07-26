##################################### Django
# Create your views here.
from .models import Stock
from . import views
from django import template
from django.template.loader import get_template
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

##################################### Quandl
import quandl

quandl.ApiConfig.api_key = 'SvgAJczTKtEuU9Fg1xJz'
quandl.ApiConfig.api_version = '2015-04-09'

##################################### Indicator Calculation
from cs103 import *
from collections import namedtuple
import matplotlib.pyplot as pyplot
import matplotlib.dates as dates
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

from django.http import HttpResponse

##################################### Django.Form

from .forms import NameForm
from django.shortcuts import render
from django.http import HttpResponseRedirect

#################################### Page: http://localhost:8000/stock/

def Index(request):
    # Introduction+ Theory
    return render(request, 'stock/index.html')

#def index(request):
#   latest_question_list = Question.objects.order_by('-pub_date')[:5]
#   template = loader.get_template('polls/index.html')
#   context = {
#       'latest_question_list': latest_question_list,
#   }
#   return HttpResponse(template.render(context, request))


#################################### Page: http://localhost:8000/stock/stockname
def Stockname(request):
    
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            stockname = "WIKI/" + str(form.cleaned_data['your_name'])
            startdate = str(form.cleaned_data['start_date'])
            stockname2 = "WIKI/" + str(form.cleaned_data['your_name2'])
            startdate2 = str(form.cleaned_data['start_date2'])
            
            stockinfo = quandl.get_table("ZACKS/FC", ticker=str(stockname))
            
            stockindicator1 = buy_sell_indicator(stock_daily(stockname, startdate), stockname)
            stockindicator2 = buy_sell_indicator(stock_daily(stockname2, startdate2), stockname2)
            
            #print(stockindicator)
            
            #Worked: HttpResponseRedirect('stock/stockindicator/')
            #Workded HttpResponse(stockname, content_type="text/plain"), return variables within the same page. 
            return stockindicator1

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        
    # should use stock/stockname.html' to direct the system to the template under stock
    return render(request, 'stock/stockname.html', {'form': form})

#################################### Page: http://localhost:8000/stock/stockindicator

def Stockindicator(request):
    
    return render(request, 'stock/stockindicator.html')

################################### Stock Indicator Logic -> Input Name/Date, Output: Image


import quandl
from cs103 import *
from collections import namedtuple
import matplotlib.pyplot as pyplot
import matplotlib.dates as dates
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

quandl.ApiConfig.api_key = 'SvgAJczTKtEuU9Fg1xJz'
quandl.ApiConfig.api_version = '2015-04-09'

Dailytrading = namedtuple("Dailytrading", ["open", "close", "volume"])

def stock_daily(stock_name, start_date):
    # stock_name = "WIKI/FB" start_date = "2016-06-30"
    # # Consume the name of the stock, and the start data of the analysis. Get the daily list from dataset WIKI:
    dataframe_stock = quandl.get(stock_name, start_date=start_date)
    # Dataslide: Get the 5 columns from the dataframe:
    dataframe_stock.ix[:,0:5]
    # Convert the data to a list."Open,High,Low,Close,Volume"
    prep_dataframe_stock = dataframe_stock.ix[:,:5] 
    stock_daily = prep_dataframe_stock.values.tolist()
    print(stock_daily)
    
    # [D1...D10]
    # print(stock_daily)
    return stock_daily

def make_dailytrading(lines):
    """
    [float, float, float] -> Dailytrading
    # template to return Dailytrading
    """
    return Dailytrading(lines[0], lines[3], lines[4])


#stock_daily [D1, D2...Dn]
def read(stock_daily):
    '''
    #  [Dailytrading] -> [tendays_trading], for example, from [D1..Dn] to [[D1..D10],....[Dn...Dn+10] ]
    '''
    dailytradings = stock_daily[::-1]
    #OK, print(dailytradings)
    # lines is a list of (the list of 3 attributes: "open", "close", "volume")
    count = 0
    tendays_trading = []
    tendays_trading_list = []
    total_row = len(stock_daily)
    #print(total_row)
    while count <= total_row and len(dailytradings[count:]) >= 10:
        start = count
        end = count + 9
        # every 10 dailytrading will form a tenday trading, then tenday trading list
        while start <= end:
        # Pn = [D1...Dn]
        # tendays_trading = tendays_trading + dailytradings
            tendays_trading = tendays_trading + [make_dailytrading(dailytradings[start])]
            start = start + 1
        #OK, print("tendays_trading" + str(tendays_trading))
        # Tn = [P1,...Pn]
        tendays_trading_list = tendays_trading_list + [(tendays_trading)]
        #OK, print("tendays_trading_list" + str(tendays_trading_list))
        count = count + 1
        tendays_trading = []
    return tendays_trading_list


def judgement(f, s):
    if f < 0 and s > 0 and abs(f) > abs(s):
        return 5 #"Buy"
    elif f < 0 and s > 0 and abs(f) < abs(s):
        return -5 #"Sell"
    elif f < 0 and s > 0 and abs(f) == abs(s):
        return 0 #"Hold"
    elif f > 0 and s < 0 and abs(f) < abs(s):
        return 5 # "Buy"
    elif f > 0 and s < 0 and abs(f) > abs(s):
        return -5 #"Sell"
    elif f > 0 and s < 0 and abs(f) == abs(s):
        return 0 #"Hold"
    elif f > 0 and s > 0 and f > s:
        return 3 #"Rising Slower"
    elif f > 0 and s > 0 and f < s:
        return 4 #"Rising Faster"
    elif f < 0 and s < 0 and f < s:
        return -3 #"Decline Slower"
    elif f < 0 and s < 0 and f > s:
        return -4 #"Decline Faster"
    
        
def first_wave(tendays_trading):
    # Part 1
    deltaprice1 = (float(tendays_trading[0].close) - float(tendays_trading[0].open))
    #print(deltaprice1)
    deltaprice2 = (float(tendays_trading[1].close) - float(tendays_trading[1].open))
    deltaprice3 = (float(tendays_trading[2].close) - float(tendays_trading[2].open))
    deltaprice4 = (float(tendays_trading[2].close) - float(tendays_trading[2].open))
    deltaprice5 = (float(tendays_trading[3].close) - float(tendays_trading[3].open))

        
    v1 = int(tendays_trading[0].volume)
    #print(v1)
    v2 = int(tendays_trading[1].volume)
    v3 = int(tendays_trading[2].volume)
    v4 = int(tendays_trading[3].volume)
    v5 = int(tendays_trading[4].volume)
        
    #  First_Half_Trading (3 days) (accumulated Wave * accumulated Volume)
    return (deltaprice1 * v1 + deltaprice2 * v2 + deltaprice3 * v3 + deltaprice4 * v4 + deltaprice5 * v5)

def second_wave(tendays_trading):
    # Part 2
    deltaprice6 = (float(tendays_trading[4].close) - float(tendays_trading[4].open))
    deltaprice7 = (float(tendays_trading[5].close) - float(tendays_trading[5].open))
    deltaprice8 = (float(tendays_trading[6].close) - float(tendays_trading[6].open))
    deltaprice9 = (float(tendays_trading[7].close) - float(tendays_trading[7].open))
    deltaprice10 = (float(tendays_trading[8].close) - float(tendays_trading[8].open))
        
    v6 = int(tendays_trading[4].volume)
    v7 = int(tendays_trading[5].volume)
    v8 = int(tendays_trading[6].volume)
    v9 = int(tendays_trading[7].volume)
    v10 = int(tendays_trading[8].volume)
        
    # Second_Half_Trading (3 days) (accumulated Wave * accumulated Volume)
    return (deltaprice6 * v6 + deltaprice7 * v7 + deltaprice8 * v8 + deltaprice9 * v9 + deltaprice10 * v10)
        
        


def calculate(tendays_trading_list):
    # [tendays_trading] -> [indicator]
    # acc is []
    acc_tendays_tradings_indicator = []
    acc_First_Half_Trading = 0
    acc_Second_Half_Trading = 0
    #print(tendays_trading_list)
    spot_indicator = [] 
    for tendays_trading in tendays_trading_list:
        acc_First_Half_Trading = first_wave(tendays_trading)
        acc_Second_Half_Trading = second_wave(tendays_trading)
        #print(acc_First_Half_Trading)
        #print(acc_Second_Half_Trading)
        # Judgement
        acc_tendays_tradings_indicator = acc_tendays_tradings_indicator + [judgement(acc_First_Half_Trading, acc_Second_Half_Trading)]
        #print(acc_tendays_tradings_indicator)

    return acc_tendays_tradings_indicator

def analysis(stock_daily):
    return calculate(read(stock_daily))



#############################################
#[D1...Dn]

def buy_sell_indicator(stock_daily, stock_name):
    # Source-> [D1...Dn]
    # draw plot(x, y1, y2)
    # dailytradings is [Dailytrading]
    dailytradings = []
    # lines is a list of (the list of 3 attributes: "open", "close", "volume")
    count = 0
    #TEST on Graph X_Axis [D1...Dn]
    date = 0
    x = []
    #TEST on Graph Y1_Axis [float...float]
    close = []
    #TEST on Graph Y1_Axis [float...float]
    volume = []
    for line in stock_daily: 
        dailytradings = dailytradings + [make_dailytrading(line)]
        #OK, print(dailytradings)
        close = close + [make_dailytrading(line).close]
        #close_reverse = close[::-1]
        volume = volume + [make_dailytrading(line).volume]
        #volume_reverse = volume[::-1]
        date = date + 1
        x = x + [date]     
    #TEST on Graph X_Axis [D1...Dn]
    # [1, 2, 3, 4, ....n]
    x_axis = np.array(x)
    print(x)
    #TEST on Graph Y1_Axis [float...float]
    y1_axis = np.array(close)
    #print(close)
    #TEST on Graph Y2_Axis [int....int]
    y2_axis = np.array(volume)
    #print(volume)
    
    
    
    #TEST 2 lines with X, Y1, Y2 
    fig, ax1 = plt.subplots()
    
    #Name the fig:
    fig.canvas.set_window_title("Buy/Sell Indicator for " + stock_name)
    #print()
    ax2 = ax1.twinx()
    ax1.plot(x_axis, y1_axis, color='indianRed')
    ax1.set_xlabel('Date Count')
    ax1.set_ylabel('Close Price', color ='indianRed')
    
    ax2.bar(x_axis, y2_axis, width=0.35, color='steelblue', align='center', alpha=0.3)
    #ax2.plot(x_axis, y2_axis, 'steelblue')
    ax2.set_ylabel('Volume', color='steelblue')
    
    #TEST on Graph Y3_Axis [int...int]
    #convert [int...int] to [0, 0, 0, 0, 0, 0, 0, 0, 0, int, 0, 0, 0, 0, 0, 0, 0, 0, 0, ...int]
    
    spot_indicator = analysis(stock_daily) #at this point the list looks like[1, 2, 3]
    spot_indicator = [0, 0, 0, 0, 0, 0, 0, 0, 0] + analysis(stock_daily)
    #print(spot_indicator)
    y3_axis = np.array(spot_indicator)
    

    #c=choose_scatter_color(spot_indicator)
    area = np.pi*3*(y3_axis)**2  # 0 to 15 point radiuses
    plt.scatter(x_axis, y3_axis, s=area, c=y3_axis, cmap="coolwarm", alpha=0.8)
    # "gist_rainbow"
    
    #plt.show()
    # return a image to httpresponse
    response=HttpResponse(content_type='image/png')
    fig.savefig(response, format='png')
    
    return response

#############################################Input Variables + Run the function. 
    
    
#stock_symbol = input('Stock Symbal: ')
#stock_name = 'WIKI/' + stock_symbol
#start_date = input('Start Date(YYYY-MM-DD): ')
#print(start_date)
#print(buy_sell_indicator(stock_daily(stock_name, start_date), stock_name))



#############################################Begin Testing
#print("READ DATA: ")
#expect(read(stock_daily), "10")
#summary() 

#print("Judgment Indicator: ")
#expect(judgement(100,  50), 4)
#expect(judgement(10,  50), 5)
#expect(judgement(100, -50), 2)
#expect(judgement(-100, -50), 6)
#expect(judgement(-10, -50), 7)
#expect(judgement(-100, 50), 1)
#summary() 

#print("Indicator List:")
#expect(analysis("test_stock.csv"), [2])
#summary() 

#print("Graph Test:")
#expect(indicator_spot(analysis("test_stock.csv")),)
#expect(historic_line("test_stock.csv"),"")
#expect(buy_sell_indicator("more_test_data.csv"),"")
#expect(buy_sell_indicator(stock_daily("WIKI/ILMN", "2016-06-14"), "WIKI/ILMN"),"")
#pyplot.reset
#expect(buy_sell_indicator(stock_daily("WIKI/DIS", "2016-06-14"), "WIKI/DIS"),"")
#expect(buy_sell_indicator(stock_daily("WIKI/TSLA", "2016-06-14"), "WIKI/TSLA"),"")
#expect(buy_sell_indicator(stock_daily("WIKI/GILD", "2016-05-14"), "WIKI/GILD"),"")
#expect(buy_sell_indicator(stock_daily("WIKI/AMZN", "2016-06-14"), "WIKI/AMZN"),"")
#expect(buy_sell_indicator(stock_daily("WIKI/AAPL", "2016-05-15"), "WIKI/AAPL"),"")
#stock_name = "WIKI/AAPL"
#start_date = "2016-06-30"

#summary()











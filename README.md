# Stock_Buy_Sale_Indicator
This website predicts the trend of stock market based on market volume.

## Installation
- Install Django
- Install pip and all dependencies

## Deployment
- run server <br>
	```
	python project_root/djangotutor/mysite/manage.py runserver
	```
	
## Motivation
This website is built to predict the trend of the stock market.
The intuition behind the scene is that if more people buy than sell the price tends to go up. This website gets realtime data from the stock market and calculate weighted average of the volumn in the past 30 days. Prediction will be made based on the calculated result.
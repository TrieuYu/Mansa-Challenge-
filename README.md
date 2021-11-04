# Prediction of next month outgoing given the past 6 months of transactions

> Code and instructions for techniques to build this prediction fucntion.

In this repo, you will find the code and instructions for my approach of this study. And there are some steps:

* Build a dataset with the account which have more than 180 days of history, and delete the duplicate data. I used only the data of transactions, because I found that the transaction.csv already provided enough information to me. I also build a function to get a time series by giving an account's ID, then I don't need to add a list of transactions recorded on the account which we want to predict its next month outgoing. 
* Build and save a ARIMA model, and a time series for each account. And why ARIMA, beacuase the the ARIMA model is a type of statistical model used to analyze and forecast time series data. It clearly caters to a set of standard structures in time series data, and therefore provides a simple and powerful method for proficient time series forecasting. We can find the detail of this model in the preprocessing notebook.
* The strengths of this approach: We will have a database for each account, and there will not have concern to mix up the data with several accounts when we build the model.
* The weaknesses of this approach: We will have a pretty bad performance so far, because we don't have that much data for each client(only an outgoing data per month).
* Possible ways to improve my predictions: 
    - We can try to make a database with the weekly outgoing data, then we will get a little more data.
    - We can try with another model which is **prophet** (also designed for automatic forecasting of univariate time series data) and we can compare these 2 models.
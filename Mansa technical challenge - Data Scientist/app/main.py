# Python 3.8.5
# Data Handling
import logging
import pickle
import numpy as np
import pandas as pd
from pydantic import BaseModel

# Server
import uvicorn
from fastapi import FastAPI

# Modeling
from statsmodels.tsa.arima.model import ARIMA, ARIMAResults

app = FastAPI()

# Initialize logging
my_logger = logging.getLogger()
my_logger.setLevel(logging.DEBUG)
# logging.basicConfig(level=logging.DEBUG, filename='sample.log')

# Initialize files of time series
ts_outgoing = pickle.load(open('data/ts_outgoing.pickle', 'rb'))
ts_account={}
for i in np.sort(ts_outgoing.account_id.unique()):
  ts_account[i] = pickle.load(open(f'data/ts_account_{i}.pickle', 'rb'))

# Initialize files of models
clf={}
for i in np.sort(ts_outgoing.account_id.unique()):
  clf[i] = ARIMAResults.load(open(f'model/arima_{i}.pkl', 'rb'))


class Data(BaseModel):
    account_id: int

@app.post("/predict")
def predict_outgoing(data: Data):
    try:
        # Get the time series of the account
        account_id = data.account_id
        ts_id = ts_account[account_id]
        train_size = int(ts_id.shape[0]*0.8)
        train, test = ts_id.iloc[0:train_size], ts_id.iloc[train_size:ts_id.shape[0]]
        
        # Create and return prediction
        predictions = pd.DataFrame(clf[account_id].forecast(test.shape[0]+1))
        # print("Prediction of the next month outgoing of this account:\n")
        return predictions[-1:]

    except:
        my_logger.error("Something went wrong!")
        return {"prediction": "This account doesn't exist in the database."}
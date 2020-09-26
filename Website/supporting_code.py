# -*- coding: utf-8 -*-
"""Supporting Code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OGwXPGteK2HG2I8V5x-2OL5VWYFTDKw2
"""

import pandas as pd
from pandas_datareader import data, wb
import datetime

start = pd.to_datetime('2015-09-24')
end = pd.to_datetime('2020-09-24')
data_df = data.DataReader('AAPL','yahoo', start, end)
df1=data_df.reset_index()['Close']
df1

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler(feature_range=(0,1))
import numpy as np
df1=scaler.fit_transform(np.array(df1).reshape(-1,1))
df1

training_size=int(len(df1)*0.80)
test_size=len(df1)-training_size
train_data,test_data=df1[0:training_size,:],df1[training_size:len(df1),:1]

#print(test_data.shape)
len(test_data)

x_input=test_data[152:].reshape(1,-1)
x_input.shape

temp_input=list(x_input)
temp_input=temp_input[0].tolist()
temp_input

# load and evaluate a saved model
from numpy import loadtxt
from keras.models import load_model
 
# load model
model = load_model(r"C:\Users\user\PycharmProjects\pythonProject1\my_model1.h5")
# summarize model.
model.summary()

from numpy import array
lst_output=[]
n_steps=100
i=0
while(i<11):
    
    if(len(temp_input)>100):
        #print(temp_input)
        x_input=np.array(temp_input[1:])
        #print("{} day input {}".format(i,x_input))
        x_input=x_input.reshape(1,-1)
        x_input = x_input.reshape((1, n_steps, 1))
        #print(x_input)
        yhat = model.predict(x_input, verbose=0)
        #yhat = scaler.inverse_transform(yhat)
        #print("{} day Prediction {}".format(i,yhat))
        temp_input.extend(yhat[0].tolist())
        temp_input=temp_input[1:]
        #print(temp_input)
        lst_output.extend(yhat.tolist())
        i=i+1
    else:
        x_input = x_input.reshape((1, n_steps,1))
        yhat = model.predict(x_input, verbose=0)
        #print(yhat[0])
        temp_input.extend(yhat[0].tolist())
        #print(len(temp_input))
        lst_output.extend(yhat.tolist())
        i=i+1

l1 = lst_output[1:11]
#print(l1)
#print(len(l1))

import itertools
b = l1
c =list(itertools.chain.from_iterable(b))
#print(c)

e = scaler.inverse_transform(b)

f = list(itertools.chain.from_iterable(e))
#print(f)
def hello():
        return f


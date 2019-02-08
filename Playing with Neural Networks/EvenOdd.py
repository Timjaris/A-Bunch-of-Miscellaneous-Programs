# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 14:47:00 2019

@author: Tim

Conclusions: This was a collosal failure, this is not the sort of things
NNs can do. NNs are basically for "plot the input on a graph, we'll find the
boundary. 

I still don't get why it won't work on a small dataset, though. I get why it 
wouldn't generalize, but a zig-zagging line should be able to learn the 
training set. 
"""
import matplotlib.pyplot as plt
import numpy as np
from keras import optimizers
from keras.models import Sequential, Model
from keras.layers import Dense, Input, Concatenate, concatenate

#datagen
def dataGen(n, t, mod):
    x = []
    y = []
    for i in range(n):
        r = np.random.randint(0, t)
        x.append(r)
        y.append([r%mod])
    x = np.array(x)
    y = np.array(y)
    return x, y

def validate(model, x, y):
    correct = 0
    total = len(y)
    pred = model.predict(x)
    for i in range(total):
        if (round(pred[i][0]) == y[i][0]):
            correct += 1
    return correct / total
            


#model def
model = Sequential()
model.add(Dense(10, input_dim=1))
model.add(Dense(10))
model.add(Dense(1, activation='softmax'))
sgd = optimizers.SGD(lr=1)
model.compile(loss='mean_squared_error', optimizer=sgd)


n = 100 # of samples
t = 10  #how many total numbers
mod = 2

xt, yt = dataGen(n, t, mod)
xv, yv = dataGen(n, t, mod)

notImproved = 0
bestAcc=0
accs = []
valAccs=[]
while notImproved < 5:
    model.fit(xt, yt, validation_data=(xv,yv))
    valAcc = validate(model, xv, yv)
    print("Val Acc =", valAcc)
    accs.append(validate(model, xt, yt))
    valAccs.append(validate(model, xv, yv))
    if valAcc > bestAcc:
        bestAcc = valAcc
        notImproved=0
    else:
        notImproved+=1
        
plt.title = "Training Accuracy"
plt.plot(accs)
plt.show()
plt.title = "Validation Accuracy"
plt.plot(valAccs)
plt.show()

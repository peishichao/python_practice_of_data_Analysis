#-*- coding:utf-8 -*-
# Peishichao
import pandas as pd

inputfile = '../data/data4.csv'
data = pd.read_csv(inputfile)

from sklearn.linear_model import Adaptivelasso
model = Adaptivelasso(gamma=1)

model.fit(data.iloc[:,0:10],data['y'])
model.coef_
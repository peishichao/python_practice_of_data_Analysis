#-*- coding:utf-8 -*-
# Peishichao

import pandas as pd

inputfile = '../data/huizong.csv'
outputfile = '../data/meidi_jd.txt'

data = pd.read_csv(inputfile,encoding='utf-8')
data = data[[u'评论']][data[u'品牌']==u'美的']
data.to_csv(outputfile,index = False, header = False)
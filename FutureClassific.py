# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from WindPy import w
#from matplotlib import pyplot as plt

# import numpy as np
#df = pd.read_excel("C:\Users\wanghao03\Desktop\Temp.xlsx")
#print df.tail(10)[['date','SettlePrice']]

#date2inx = {}
#
#for i in range(len(df)):
#    date2inx[i] = df.iloc[i]['date']
    
#date = []
#for dt in df[3:13]['date']:
#    dt = str(dt)
#    dt = int(dt[8:10])
#    date.append(dt)
    
    




#labelFuture = {}
#for i in range(3,2127):
#    charge = df.iloc[i-3]['SettlePrice'] - df.iloc[i+3]['SettlePrice']
#    if abs(charge) < 87:
#        labelFuture[i] = "fluc"
#    elif charge < 0:
#        labelFuture[i] = "rise"
#    elif charge > 0:
#        labelFuture[i] = "fall"
#
#i = 0
#for item in labelFuture:
#    if i < 100:
#        print item,df.iloc[item]['date'],df.iloc[item]['SettlePrice'],labelFuture[item]
#        i = i + 1
#    
#plt.title("Future trend")
#plt.xlabel("date")
#plt.ylabel("Settlement Price")
#plt.plot(range(10),df.head(10)['SettlePrice'],"ro-")
#plt.ylim((3550, 3700))
#plt.show()

# 计算差价列表平均数
#print len(priceAbs)
#print reduce(lambda x, y: x + y, priceAbs) / len(priceAbs)

class FutureChange():
    def __init__(self,src):
        self._src = src
        
    def Dealdata(_src,src):
        df = pd.read_excel(src)
        df = df.drop(df.index[-2:])
        date2inx = {}
        labelFuture = {}
        priceAbs = []
        for i in range(len(df)):
            date2inx[i] = df.iloc[i][u'日期']
        for i in range(3,len(df)-3):
            diff = df.iloc[i-3][u'结算价'] - df.iloc[i+3][u'结算价']
            priceAbs.append(abs(diff))
        avg = reduce(lambda x, y: x + y, priceAbs) / len(priceAbs)
        print avg
        for i in range(3,len(df)-3):
            diff = df.iloc[i-3][u'结算价'] - df.iloc[i+3][u'结算价']
            if abs(diff) < avg:
                labelFuture[i] = "fluc"
            elif diff < 0:
                labelFuture[i] = "rise"
            elif diff > 0:
                labelFuture[i] = "fall"
        i = 0
        for item in labelFuture:
            if i < 150:
                print item,df.iloc[item][u'日期'],df.iloc[item][u'结算价'],labelFuture[item]
                i = i +  1
    
    #def showRst():
            
#d = w.wsd("RB1801.SHF", "settle", "2000-01-01", "2017-12-25", "")
    
    
c = FutureChange("C:\Users\wanghao03\Desktop\M1811-DCE.xlsx")   
c.Dealdata("C:\Users\wanghao03\Desktop\M1811-DCE.xlsx")
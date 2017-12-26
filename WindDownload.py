# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 15:35:05 2017

@author: wanghao03
"""

#import pandas as pd
#from datetime import datetime
from WindPy import w


w.start()
#d = w.wsd("RB1801.SHF", "settle", "2017-01-15", "2017-12-25", "")




#df = pd.DataFrame(d.Data,index=['SettlePrice'],columns=d.Times)
#df = df.T
#print df.head(10)


# 上期所，大商所以及郑商所商品合约代码
shfe = ['CU','AL','ZN','PB','NI','SN','AU','AG',
      'RB','WR','HC','FU','BU','SC','RU','IM']
dce = ['M','Y','A','B','P','C','CS','JD',
       'BB','FB','L','V','PP','J','JM','I']
czce = ['SR','CF','ZC','FG','TA','MA','WH','PM',
        'RI','LR','JR','RS','OI','RM','SF','SM','CY','AP']
        
s = w.wset("futurecc","wind_code=M.DCE;field=wind_code,contract_issue_date")
item = {}
for i in range(len(s.Data[0])):
    item[s.Data[0][i]] = s.Data[1][i]
    

print len(s.Data[0])
j = 0
for k in item:
    print k,'\t',item[k],'\n'
    

d = w.wsd("M1801.DCE","settle",item["M1801.DCE"].strftime("%Y-%m-%d"),"2017-12-25","")
print d
        
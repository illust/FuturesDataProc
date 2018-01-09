# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 15:35:05 2017

@author: svenwong
"""

import pandas as pd
import FutureClassific
from WindPy import w

w.start()

# 上期所，大商所以及郑商所商品合约代码
shf = ['CU','AL','ZN','PB','NI','SN','AU','AG',
      'RB','WR','HC','FU','BU','SC','RU','IM']
dce = ['M','Y','A','B','P','C','CS','JD',
       'BB','FB','L','V','PP','J','JM','I']
czce = ['SR','CF','ZC','FG','TA','MA','WH','PM',
        'RI','LR','JR','RS','OI','RM','SF','SM','CY','AP']
  
class WindData:

    df = pd.DataFrame()
    cntStr = []
    def __init__(self,exchange,count):
        self.exchange = exchange
        self.count = count
        
    def SetCnt(self):
       if self.exchange == 'shf':
           for i in range(len(shf)):
               self.cntStr.append(shf[i] + '.' + self.exchange.upper())
       elif self.exchange == 'dce':
           for i in range(len(dce)):
               self.cntStr.append(dce[i] + '.' + self.exchange.upper())
       elif self.exchange == 'czce':
           for i in range(len(czce)):
               self.cntStr[i].append(czce[i] + '.' + self.exchange.upper())
                        # -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 15:35:05 2017

@author: svenwong
"""

import pandas as pd
import FutureClassific
from WindPy import w

w.start()

# 上期所，大商所以及郑商所商品合约代码
shf = ['CU','AL','ZN','PB','NI','SN','AU','AG',
      'RB','WR','HC','FU','BU','SC','RU','IM']
dce = ['M','Y','A','B','P','C','CS','JD',
       'BB','FB','L','V','PP','J','JM','I']
czc = ['SR','CF','ZC','FG','TA','MA','WH','PM',
        'RI','LR','JR','RS','OI','RM','SF','SM','CY','AP']
 
 # WindData类的功能：对于用户输入的交易所缩写，打印其所有商品合约指定数量的交易日期、成交价以及涨跌情况
class WindData:

    df = pd.DataFrame()
    cntStr = [] # 交易所所有商品代码，如['CU.SHF','AL.SHF',...]
    def __init__(self,exchange,count=10):
        self.exchange = exchange
        self.count = count
        
    def SetCnt(self):
       if self.exchange == 'shf':
           for i in range(len(shf)):
               self.cntStr.append(shf[i] + '.' + self.exchange.upper())
       elif self.exchange == 'dce':
           for i in range(len(dce)):
               self.cntStr.append(dce[i] + '.' + self.exchange.upper())
       elif self.exchange == 'czc':
           for i in range(len(czc)):
               self.cntStr.append(czc[i] + '.' + self.exchange.upper())
                        
                    
    def DataCollect(self):
        # 对交易所内所有商品进行迭代
        for i in range(len(self.cntStr)):
            # wset()返回某一商品所有合约数据集，例如商品代码M.DCE代表大商所豆粕
            s = w.wset("futurecc","wind_code=%s;field=wind_code,contract_issue_date,last_trade_date"%self.cntStr[i])
            print self.cntStr[i]
            item = {} # item字典用于将合约代码与[上市日期，最后交易日期]构建字典
            for j in range(len(s.Data[0])):
                item[s.Data[0][j]] = [s.Data[1][j],s.Data[2][j]]
                
            # 对某一商品所有交易合约进行迭代
            for k in range(len(s.Data[0])):
                d = w.wsd(s.Data[0][k],"settle",item[s.Data[0][k]][0].strftime("%Y-%m-%d"),item[s.Data[0][k]][1].strftime("%Y-%m-%d"),"")
                print s.Data[0][k]
                
                # 构建pandas.DataFrame结构                
                date = []
                settlePrice = []
                for i in range(len(d.Times)):
                    date.append(d.Times[i].strftime("%Y-%m-%d"))
                    settlePrice.append(d.Data[0][i])
                data = {u'日期':date,u'结算价':settlePrice}
                df = pd.DataFrame(data)
                
                # 实例化FutureChange类，分析每个交易日的涨跌或者波动
                fc = FutureClassific.FutureChange(df,self.count)
                fc.Dealdata()
                fc.ChangeClassific()
                fc.PrintChg()
                print '\n'
    
        
if __name__ == "__main__":
    wd = WindData('czc',30)
    wd.SetCnt()
    df = wd.DataCollect()




                    
    def DataCollect(self):
        for i in range(len(self.cntStr)):
            # wset()返回某一商品所有合约数据集，例如商品代码M.DCE代表大商所豆粕
            s = w.wset("futurecc","wind_code=%s;field=wind_code,contract_issue_date,last_trade_date"%self.cntStr[i])
            print self.cntStr[i]
            item = {} # item字典用于将合约代码与[上市日期，最后交易日期]构建键值对
            for j in range(len(s.Data[0])):
                item[s.Data[0][j]] = [s.Data[1][j],s.Data[2][j]]
                
    
            for k in range(len(s.Data[0])):
                d = w.wsd(s.Data[0][k],"settle",item[s.Data[0][k]][0].strftime("%Y-%m-%d"),item[s.Data[0][k]][1].strftime("%Y-%m-%d"),"")
                print s.Data[0][k]
                # 构建pandas.DataFrame结构                
                date = []
                settlePrice = []
                for i in range(len(d.Times)):
                    date.append(d.Times[i].strftime("%Y-%m-%d"))
                    settlePrice.append(d.Data[0][i])
                data = {u'日期':date,u'结算价':settlePrice}
                df = pd.DataFrame(data)
                
                fc = FutureClassific.FutureChange(df,self.count)
                fc.Dealdata()
                fc.ChangeClassific()
                fc.PrintChg()
                print '\n'
    
        


if __name__ == "__main__":
    wd = WindData('dce',20)
    wd.SetCnt()
    df = wd.DataCollect()




# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 15:35:05 2017

@author: svenwong
"""
import pandas as pd
# from WindPy import w

class FutureChange:

    labelFuture = {}  # labelFuture用于将索引与某合约自上市以来所有的交易日（首尾共计六天除外）构建键值对。
    df = pd.DataFrame()
    avg = 0
    
    def __init__(self,df,cnt):
       
        self.df = df
        self.cnt = cnt
        
    def Dealdata(self):
        
        date2inx = {} # date2inx[]用于构建索引与日期键值对
        priceAbs = [] # priceAbs用于存放某合约所有交易日周期内首尾交易日结算价差价(TSPD)
        
        for i in range(len(self.df)):
            date2inx[i] = self.df.iloc[i][u'日期']
            
        # 这里使用的基本策略是：判断某一交易日的涨跌情况，选择其结算价指标，并采用某交易日的前第三天与后第三天的TSPD作为涨跌分类指标，
        # 计算TSPD的平均值是考虑到有些TSPD值较小，可以将交易日的涨跌情况归类为波动，平均值起到阈值的作用
        for i in range(3,len(self.df)-3):
            diff = self.df.iloc[i-3][u'结算价'] - self.df.iloc[i+3][u'结算价'] 
            priceAbs.append(abs(diff))
        
        self.avg = reduce(lambda x, y: x + y, priceAbs) / len(priceAbs) # 计算差价均值
        
    # 给每个交易日的涨跌情况分类：上涨rise,下跌fall,波动fluc
    def ChangeClassific(self):
        for i in range(3,len(self.df)-3):
            diff = self.df.iloc[i-3][u'结算价'] - self.df.iloc[i+3][u'结算价']

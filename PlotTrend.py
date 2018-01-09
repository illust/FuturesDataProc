# -*- coding: utf-8 -*-
"""
Created on Mon Jan 8 13:44:36 2018

@author: wanghao03
"""
import pandas as pd
from WindPy import w
import numpy as np
import FutureClassific
from matplotlib import pyplot as plt 

# Interactioin这个类实现的功能：对于用户输入的交易代码，打印指定数量的交易日期、成交价以及涨跌情况，并进行可视化
class Interaction:

    df = pd.DataFrame()
    def __init__(self,wd,count=10):
        self.wd_code = wd  # 商品交易合约代码
        self.count = count # 显示数目

    def format(self):
        str = self.wd_code.split(".")[0][:-4]+"."+self.wd_code.split(".")[1]
        
        # 获取某商品所有合约代码以及合约上市日，最后交易日
        s = w.wset("futurecc","wind_code=%s;field=wind_code,contract_issue_date,last_trade_date"%str)

        # ci_dates(concract_issue_date)即合约上市日，lt_date(last_trade_date)即最后交易日
        self.ci_date = s.Data[1][s.Data[0].index(self.wd_code)]
        self.lt_date = s.Data[2][s.Data[0].index(self.wd_code)]

        # 获取某商品某一完成合约在其每个交易日内成交价信息
        d = w.wsd(self.wd_code,"settle",self.ci_date.strftime("%Y-%m-%d"),self.lt_date.strftime("%Y-%m-%d"))

        # 构建pandas.DataFrame结构                
        date = []
        settlePrice = []
        for i in range(len(d.Times)):
            date.append(d.Times[i].strftime("%Y-%m-%d"))
            settlePrice.append(d.Data[0][i])
        data = {u'日期':date,u'结算价':settlePrice}
        self.df = pd.DataFrame(data)

        # 实例化FutureChange类，分析每个交易日的涨跌或者波动
        fc = FutureClassific.FutureChange(self.df,self.count)
        fc.Dealdata()
        fc.ChangeClassific()
       
        # 为df添加"涨跌情况"一列信息
        lfe = []
        for item in fc.labelFuture:
            lfe.append(fc.labelFuture[item])
        self.df[u'涨跌情况'] = lfe
        print self.df
        

    def plot(self):
        # date = [] date用于存放日期作为横坐标，但是数据量多不易显示，故舍弃
        settle = [] # settle用于存放结算价作为纵坐标
        index = np.arange(0,len(self.df)/12)
        print self.df
        for i in np.arange(0,len(self.df)/12):
            #fd = self.df.iloc[i][u'日期'].split('-')[1]+self.df.iloc[i][u'日期'].split('-')[1]
            #date.append(fd)
            settle.append(self.df.iloc[i][u'结算价'])

        # 绘图
        plt.plot(index,settle,'ro-',label='future change')
        legend = plt.legend(loc='upper center',shadow=True, fontsize='x-large')
        # Put a nicer background color on the legend.
        legend.get_frame().set_facecolor('#00FFCC')
        plt.show()

def main():
    w.start()
    ia = Interaction("RB1801.SHF")
    ia.format()
    ia.plot()

if __name__ == '__main__':
    main()
        # mulds = []
        # for item in range(0,len(fc.df)):
        #     mulds.append({fc.df.iloc[item][u'日期']:[fc.df.iloc[item][u'结算价'],fc.labelFuture[item]]})
        lfe = []
        for item in fc.labelFuture:
            lfe.append(fc.labelFuture[item])
        self.df[u'涨跌情况'] = lfe
        print self.df
        

    def plot(self):
        # date = []
        settle = []
        index = np.arange(0,len(self.df)/12)
        print self.df
        for i in np.arange(0,len(self.df)/12):
            #fd = self.df.iloc[i][u'日期'].split('-')[1]+self.df.iloc[i][u'日期'].split('-')[1]
            #date.append(fd)
            settle.append(self.df.iloc[i][u'结算价'])
        plt.plot(index,settle,'ro-',label='future change')
        legend = plt.legend(loc='upper center',shadow=True, fontsize='x-large')
        # Put a nicer background color on the legend.
        legend.get_frame().set_facecolor('#00FFCC')
        plt.show()

def main():
    w.start()
    ia = interaction("RB1701.SHF")
    ia.format()
    ia.plot()

if __name__ == '__main__':
    main()

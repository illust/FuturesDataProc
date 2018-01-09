# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 13:44:36 2018

@author: wanghao03
"""
import pandas as pd
from WindPy import w
import numpy as np
import FutureClassific
from matplotlib import pyplot as plt 


class interaction:

    df = pd.DataFrame()

    def __init__(self,wd,count=10):
        self.wd_code = wd
        self.count = count

    def format(self):
        str = self.wd_code.split(".")[0][:-4]+"."+self.wd_code.split(".")[1]
        # wd_code即合约代码，ci_dates(concract_issue_date)即合约上市日，lt_date(last_trade_date)即最后交易日)
        s = w.wset("futurecc","wind_code=%s;field=wind_code,contract_issue_date,last_trade_date"%str)
        self.ci_date = s.Data[1][s.Data[0].index(self.wd_code)]
        self.lt_date = s.Data[2][s.Data[0].index(self.wd_code)]
        d = w.wsd(self.wd_code,"settle",self.ci_date.strftime("%Y-%m-%d"),self.lt_date.strftime("%Y-%m-%d"))
        # 构建pandas.DataFrame结构                
        date = []
        settlePrice = []
        for i in range(len(d.Times)):
            date.append(d.Times[i].strftime("%Y-%m-%d"))
            settlePrice.append(d.Data[0][i])
        data = {u'日期':date,u'结算价':settlePrice}
        self.df = pd.DataFrame(data)
        fc = FutureClassific.FutureChange(self.df,self.count)
        fc.Dealdata()
        fc.ChangeClassific()
        # 构建[{date:[settle,up_or_d]}]
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
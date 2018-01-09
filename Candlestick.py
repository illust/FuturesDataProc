# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 13:44:36 2018

@author: wanghao03
"""
import tushare as ts
import matplotlib.pyplot as plt 
import matplotlib.finance as mpf
import pandas as pd
from WindPy import w
import numpy as np
import urllib
import matplotlib.dates as mdates

#w.start()



# 此脚本用于绘制蜡烛图


def bytedate2num(fmt):
    def converter(b):
        return mdates.strpdate2num(fmt)(b.decode('ascii'))
    return converter

# 从Wind获取期货相关指标：开盘价、最高价、最低价、收盘价、成交量、成交额以及结算价
#d = w.wsd("RB1801.SHF",  "open,high,low,close,volume,amt,settle", "2017-12-10", "2018-01-08", "")

# 设置历史数据区间
date1 = (2014,12,1)
date2 = (2016,12,1)

# 从雅虎财经中获取股票代码601558的历史行情
# 雅虎API不可用
# quotes = mpf.quotes_historical_yahoo_ohlc('601558.ss', date1, date2)
# 参考https://pythonprogramming.net/candlestick-ohlc-graph-matplotlib-tutorial/

stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
source_code = urllib.urlopen(stock_price_url).read().decode()
stock_data = []
split_source = source_code.split('\n')
for line in split_source[1:]:
    split_line = line.split(',')
    if len(split_line) == 7:
        if 'values' not in line and 'labels' not in line:
            stock_data.append(line)

    
date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
                                                      delimiter=',',
                                                      unpack=True,
                                                      converters={0: bytedate2num('%Y-%m-%d')})

x = 0
y = len(date)
ohlc = []

while x < y:
	append_me = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
	ohlc.append(append_me)
	x+=1

# 创建一个子图
fig,ax = plt.subplots(facecolor=(0.5,0.5,0.5))
fig.subplots_adjust(bottom=0.2)

# 设置x轴刻度为日期时间
ax.xaxis_date()
# x轴刻度文字倾斜45度
plt.xticks(rotation=45)
plt.title("股票代码：601558两年k线图")
plt.xlabel("时间")
plt.ylabel("股价（元）")
mpf.candlestick_ohlc(ax, ohlc,width=1.2,colorup='r',colordown='green')
plt.grid(True)
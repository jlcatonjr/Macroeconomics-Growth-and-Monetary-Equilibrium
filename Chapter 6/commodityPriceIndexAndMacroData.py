import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like

import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.backends.backend_pdf import PdfPages
from statsmodels.tsa.api import VAR, DynamicVAR

def plotDF(df, names,pp, title="", secondary_y=None, logy=False, legend=False, dataType="",
           start=None,end=None, importantYears = None):
    plt.rcParams['axes.ymargin'] = 0
    plt.rcParams['axes.xmargin'] = 0
    plotDict = {}
    color = ["k", "r", "C0","C2"]
    fig, ax1 = plt.subplots(figsize=(12,6))
    ax2 = ax1.twinx()   # mirror them
    for i in range(len(names)):
        if i + 1 < len(names):
            plotDict["ln" + str(i)] = ax1.plot(df[names[i]][start:end], color = color[i])
        else:
            plotDict["ln" + str(i)] = ax2.plot(df[names[i]][start:end], color = color[i])
            
    ax1.tick_params(axis='x', rotation=90)
    
    for i in range(len(names)):
        if i == 0:
            lns = plotDict["ln" + str(i)] 
        else:            
            lns += plotDict["ln" + str(i)] 
    labs = [l.get_label() for l in lns]
    ax1.legend(lns, labs, bbox_to_anchor=(.77,1.15), loc=2)
    if importantYears != None:
        for year in importantYears:
            plt.axvline(year, color="k",ls= "--")
        plt.axhline(0, color = "k", ls = "--", linewidth = .5)
#    plt.xticks(rotation=90)
#    plt.xlabel(df.index.name, fontsize=18)
    if title == "":
        if len(names) < 2:
            plt.title(names[0], fontsize=24)
    else:
        plt.title(title)
    plt.gcf()
    if start == None:start=""
    if end == None: end = ""
    plt.savefig(str(names).replace('[',' ').replace(']',' ')+ dataType + " " +\
                str(start).replace(":","") + "-" + str(end).replace(":","")+ '.png'
                ,bbox_inches="tight")
    plt.show()
    pp.savefig(fig)
    plt.close()

start = datetime.datetime(2000, 1, 1)
end = datetime.datetime(2018, 6, 1)

dfDict = {}
goldDict = {}
dfDict["Data"]  = web.DataReader("GDPC1", "fred", start, end).resample("Q").first()
dfDict["Data"] = dfDict["Data"].rename(columns = {"GDPC1":"Real GDP (Billions)"})
dfDict["Data"]["GDP Deflator"] = web.DataReader("GDPC1", "fred", start, end).resample("Q").first()
dfDict["Data"]["Commodity Price Index"] = web.DataReader("PALLFNFINDEXQ", "fred", start, end).resample("Q").first()

goldDict["Gold Data"] = pd.DataFrame.from_csv("goldPriceAndStock.csv").dropna()
goldDict["Gold Data (Logged)"] = np.log(goldDict["Gold Data"])
goldDict["Gold Data (Growth Rate)"] = goldDict["Gold Data (Logged)"].diff()
goldDict["Gold Data (Growth Rate)"]["Real Gold Price"] = goldDict["Gold Data"]["Real Gold Price"]
pp = PdfPages("Global Commodity Price Index")
names = ["Commodity Price Index", "Real GDP (Billions)"]
plotDF(dfDict["Data"], names,pp, title="", secondary_y="Real GDP (Billions)", logy=False, legend=True, dataType="",
           start=start,end=end)

start = datetime.datetime(1855, 1, 1)
end = datetime.datetime(1940, 1, 1)
names = list(goldDict["Gold Data"].keys())[:2] #["Total Gold Stock","Real Gold Price", ]
title = "Real Gold Price and Percent Change in Quantity"
importantYears = ["1914", "1919", "1929"]
for key in goldDict:
    plotDF(goldDict[key], names,pp, title=title, secondary_y="Real Gold Price", logy=False, legend=True, dataType="",
               start=start,end=end, importantYears=importantYears)
    
start = datetime.datetime(1913, 1, 1)
#end = datetime.datetime(1940, 1, 1)
names = ["Real Gold Price", "% World Gold Held by CB"]
title = "Fluctuations in Gold Price and Quantity"
importantYears = ["1914", "1919", "1927"]
for key in goldDict:
    plotDF(goldDict[key], names,pp, title=title, secondary_y="Total Gold Stock", logy=False, legend=True, dataType="",
               start=start,end=end, importantYears=importantYears)

pp.close()

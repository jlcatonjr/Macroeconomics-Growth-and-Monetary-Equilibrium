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
    fig, ax1 = plt.subplots(figsize=(24,12))
#    ax2 = ax1.twinx()   # mirror them
    for i in range(len(names)):
        if i + 1 < len(names):
            plotDict["ln" + str(i)] = ax1.plot(df[names[i]][start:end], color = color[i])
        else:
            plotDict["ln" + str(i)] = ax1.plot(df[names[i]][start:end], color = color[i])
            
    ax1.tick_params(axis='x', rotation=90)
    
    for i in range(len(names)):
        if i == 0:
            lns = plotDict["ln" + str(i)] 
        else:            
            lns += plotDict["ln" + str(i)] 
    labs = [l.get_label() for l in lns]
    ax1.legend(lns, labs, bbox_to_anchor=(.6,1.15), loc=2)
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

start = datetime.datetime(1950, 1, 1)
end = datetime.datetime(2018, 6, 1)
pp = PdfPages("Fisher Equation Data.pdf")
dfDict = {}
goldDict = {}
dfDict["Data"]  = web.DataReader("CPIAUCNS", "fred", start, end).resample("M").first()
dfDict["Data"] = dfDict["Data"].rename(columns = {"CPIAUCNS":"Consumer Price Index"})
dfDict["Data"]["3 Month Treasury Interest Rate"] = web.DataReader("TB3MS", "fred", start, end).resample("M").first()
dfDict["Data"]["Annualized Inflation Rate (CPI, Monthly)"] = np.log(dfDict["Data"]["Consumer Price Index"]).diff(12) * 100 #(1 + (dfDict["Data"]["Consumer Price Index"].diff() / dfDict["Data"]["Consumer Price Index"]).dropna())**12 - 1
plotDF(dfDict["Data"], ["Annualized Inflation Rate (CPI, Monthly)","3 Month Treasury Interest Rate"],pp=pp, secondary_y=None)
pp.close()

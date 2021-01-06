import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like

import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.backends.backend_pdf import PdfPages
from statsmodels.tsa.api import VAR, DynamicVAR
import copy

def plotDF(df, names,pp, title="", secondary_y=None, logy=False, legend=False, dataType="",
           start=None,end=None):
#    start = df.index[0]
    plt.rcParams['axes.ymargin'] = 0
    plt.rcParams['axes.xmargin'] = 0
    
    fig, ax1 = plt.subplots(figsize=(24,12))
#    vlineYear = datetime.datetime(2008, 10, 31)
#    plt.axhline(vlineYear,color="k",ls="--")
    #plot data synced to different y-axes
    lns=[]  
    if secondary_y != None:
        ax2 = ax1.twinx()        
    for i in range(len(names)):
        name = names[i]

        if name != secondary_y:
            lns.append(ax1.plot(df[name])[0])
        
            
        else:
##            if "Divisia" in name:
##                lns.append(ax2.plot(df[name], ls="--", linewidth=3)[0])
#            else:
            lns.append(ax2.plot(df[name], ls="-",color="C3", label=name + (" (right)"))[0])
 
    #Rotate date labels
    ax1.tick_params(axis='x', rotation=90)

    labs = [ln.get_label() for ln in lns]
    
#    for i in range(len(labs)):
#        print(labs[i])
#        if labs[i] == secondary_y:
#            labs[i] = labs[i] + " (right)"
    plt.rcParams.update({'legend.fontsize': 22,'legend.handlelength': 2})
#    ax1.legend(lns, labs, bbox_to_anchor=(.73 ,1.025 + .05 * len(labs)), loc=2)  
    ax1.legend(lns, labs, bbox_to_anchor=(.0, -.085 - .002 * len(labs)), loc=2)  

#    ax1.legend(lns, labs, bbox_to_anchor=(.815, 1.025 + .05 * len(labs)), loc=2)  
    plt.title(title)
#    ax1.legend(lns, labs, bbox_to_anchor=(.64, 1.025 + .05 * len(labs)), loc=2)  
#    df[keys].plot.line(figsize=(24,12), legend=False, secondary_y = keys[0])
#    plt.title(str(keys).replace("[","").replace("]",""), fontsize=40)



#    fig = df[names][start:end].plot.line(logy=logy, secondary_y=secondary_y, legend=legend,figsize=(10,6), color=['k', 'C3','C0'], fontsize=14).get_figure()
#    if any([("Rate" in name) for name in names])  : plt.axhline(0, color="k", ls="--", linewidth=1)
#    plt.xticks(rotation=90)
#    plt.xlabel(df.index.name, fontsize=18)
#    if title == "":
#        if len(names) < 2:
#            plt.title(names[0], fontsize=24)
#    else:
#        plt.title(title)
#    plt.gcf()
    if start == None:start=""
    if end == None: end = ""
    plt.savefig(dataType + " " + str(start).replace(":","") + "-" + str(end).replace(":","")+ " " +
                str(names).replace('[',' ').replace(']',' Secondary Y = ' + str(secondary_y) + '.png'),bbox_inches="tight")
    plt.show()
    pp.savefig(fig, bbox_inches="tight")
    plt.close()
start = datetime.datetime(1947, 1, 1)
end = datetime.datetime(2018, 7, 1)
plt.rcParams.update({'font.size': 22})

dfDict = {}
goldDict = {}
dfDict["Quarterly"]  = web.DataReader("GDPC1", "fred", start, end).resample("Q").first()
dfDict["Quarterly"] = dfDict["Quarterly"].rename(columns = {"GDPC1":"Real GDP (Billions)"})
dfDict["Quarterly"]["GDP Deflator"] = web.DataReader("GDPC1", "fred", start, end).resample("Q").first()
dfDict["Quarterly"]["Real Imports"] = web.DataReader("IMPGSC1", "fred", start, end).resample("Q").first()
dfDict["Quarterly"]["Real Exports"] = web.DataReader("EXPGSC1", "fred", start, end).resample("Q").first()
dfDict["Quarterly"]["Net Exports"] = dfDict["Quarterly"]["Real Exports"] - dfDict["Quarterly"]["Real Imports"]

dfDict["Logged Quarterly"] = np.log(dfDict["Quarterly"])
dfDict["Year Over Year Rate (Quarterly)"] = web.DataReader("GDPC1", "fred", start, end).resample("Q").first()
dfDict["Year Over Year Rate (Quarterly)"] = dfDict["Year Over Year Rate (Quarterly)"].rename(columns = {"GDPC1":"Real GDP"})


for key in dfDict["Quarterly"]:
    if "Rate" not in key:
        dfDict["Year Over Year Rate (Quarterly)"][key] = dfDict["Quarterly"][key].pct_change(periods=4)
    else:
        print("Rate is in this key:", key)
        dfDict["Year Over Year Rate (Quarterly)"][key] = dfDict["Quarterly"][key]
        
dfDict["Year Over Year Rate (Quarterly)"] = dfDict["Year Over Year Rate (Quarterly)"].dropna()


pp = PdfPages("International Trade Data.pdf")

for key in dfDict:
    names = ["Real Imports", "Real Exports", "Real GDP (Billions)"]

    plotDF(dfDict[key], names,pp, title=key, secondary_y="Real GDP (Billions)", logy=False, legend=True, dataType=key,
           start=start,end=end)


    names = ["Real Imports", "Real Exports", "Net Exports"]
    plotDF(dfDict[key], names,pp, title=key, secondary_y="Net Exports", logy=False, legend=True, dataType=key,
               start=start,end=end)
start = datetime.datetime(1999, 1, 1)
end = datetime.datetime(2018, 4, 1)
plt.rcParams.update({'font.size': 22})

dfDict2 = {}
dfDict2["Quarterly"]  = web.DataReader("IEABC", "fred", start, end).resample("Q").first()
dfDict2["Quarterly"] = dfDict2["Quarterly"].rename(columns = {"IEABC":"Current Account Balance"})
dfDict2["Quarterly"]["Capital Account Balance"]  = web.DataReader("RWLBCAQ027S", "fred", start, end).resample("Q").first()
dfDict2["Logged Quarterly"] = np.log(dfDict2["Quarterly"])
dfDict2["Year Over Year Rate (Quarterly)"] = web.DataReader("GDPC1", "fred", start, end).resample("Q").first()
for key in dfDict2["Quarterly"]:
    if "Rate" not in key:
        dfDict2["Year Over Year Rate (Quarterly)"][key] = dfDict2["Quarterly"][key].pct_change(periods=4)
    else:
        print("Rate is in this key:", key)
        dfDict2["Year Over Year Rate (Quarterly)"][key] = dfDict2["Quarterly"][key]

for key in dfDict2:
    names = ["Current Account Balance", "Capital Account Balance"]

    plotDF(dfDict2[key], names,pp, title=key, secondary_y="Capital Account Balance", logy=False, legend=True, dataType=key,
           start=start,end=end)

#
##names = list(goldDict["Gold Data"].keys())[:2] #["Total Gold Stock","Real Gold Price", ]
#title = "Real Gold Price and Percent Change in Quantity"
#importantYears = ["1914", "1919", "1929"]
#for key in goldDict:
#    plotDF(goldDict[key], names,pp, title=title, secondary_y="Real Gold Price", logy=False, legend=True, dataType="",
#               start=start,end=end, importantYears=importantYears)
#    
#start = datetime.datetime(1913, 1, 1)
##end = datetime.datetime(1940, 1, 1)
#names = ["Real Gold Price", "% World Gold Held by CB"]
#title = "Fluctuations in Gold Price and Quantity"
#importantYears = ["1914", "1919", "1927"]
#for key in goldDict:
#    plotDF(goldDict[key], names,pp, title=title, secondary_y="Total Gold Stock", logy=False, legend=True, dataType="",
#               start=start,end=end, importantYears=importantYears)

pp.close()

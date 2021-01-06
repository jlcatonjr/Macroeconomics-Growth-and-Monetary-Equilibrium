import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like

import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import numpy as np
import os
import copy
from matplotlib.backends.backend_pdf import PdfPages

def plotDF(df, names,pp, title="", secondary_y=None, logy=False, legend=False, dataType="",
           start=None,end=None):
#    start = df.index[0]
    plt.rcParams['axes.ymargin'] = 0
    plt.rcParams['axes.xmargin'] = 0
    
    fig, ax1 = plt.subplots(figsize=(24,12))
    vlineYear = datetime.datetime(2008, 10, 31)
    plt.axvline(vlineYear,color="k",ls="--")
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
            lns.append(ax2.plot(df[name], ls="--",color="C2", label=name + (" (right)"))[0])
        if "Divisia" in name:
            plt.axhline(max(df[name]), color = "k", ls = "--", linewidth = .5)
            plt.axhline(min(df[name]), color = "k", ls = "--", linewidth = .5)
    
    #Rotate date labels
    ax1.tick_params(axis='x', rotation=90)

    labs = [ln.get_label() for ln in lns]
    
#    for i in range(len(labs)):
#        print(labs[i])
#        if labs[i] == secondary_y:
#            labs[i] = labs[i] + " (right)"
    plt.rcParams.update({'legend.fontsize': 22,'legend.handlelength': 2})
#    ax1.legend(lns, labs, bbox_to_anchor=(.73 ,1.025 + .05 * len(labs)), loc=2)  
    ax1.legend(lns, labs, bbox_to_anchor=(.0, 0 - .05 * len(labs)), loc=2)  

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

def scatterPlot(df, key1,key2,pp,dataType, title=""):
    fig,ax = plt.subplots(figsize=(24,12))
    plt.scatter(x=df[key1], y=df[key2], s = 10**2)
    plt.axhline(0, ls = "--", color="k", linewidth = 1)
    plt.axvline(0, ls="--", color="k", linewidth = 1)
    ax.set_xlabel(key1)
    ax.set_ylabel(key2)
    dfk1 = df[key1].dropna()
    minDFK1 = min(dfk1)
    maxDFK1 = max(dfk1)
    dfk2 = df[key2].dropna()
    minDFK2 = min(dfk2)
    maxDFK2 = max(dfk2)

    ax.set_xlim(minDFK1 - .01 * abs(minDFK1), maxDFK1 + .01 * abs(maxDFK1))
    ax.set_ylim(minDFK2 - .01 * abs(minDFK2),maxDFK2 + .01 * abs(maxDFK2))
    plt.title(title)
    plt.savefig(dataType + " " + str(start).replace(":","") + "-" + str(end).replace(":","")+ " " +
            key1 + " " + key2 +'scatter.png', bbox_inches="tight")
    plt.show()
    pp.savefig(fig, bbox_inches="tight")
    plt.close()


def buildSummaryCSV(fullPredictResults, csvName, folder):
    try:
        os.mkdir(folder)
    except:
        print(folder, "already exists")
    predictorModelResults= str(fullPredictResults.summary())
    file = open(folder + "\\" + csvName + ".csv" ,"w")
    file.write(predictorModelResults)
    file.close()

plt.rcParams.update({'font.size': 22})
pp = PdfPages("FedPlots.pdf")
start = datetime.datetime(1948, 1, 1)
end = datetime.datetime(2018, 10, 1)
dfDict = {}

dfDict["Monthly"] = web.DataReader("UNRATE", "fred",start, end).resample("M").first() / 100
dfDict["Monthly"] = dfDict["Monthly"].rename(columns = {"UNRATE":"Unemployment Rate"})
dfDict["Monthly"]["Natural Rate of Unemployment"] = web.DataReader("NROU", "fred",start, end).resample("M").first() / 100
dfDict["Monthly"]["Labor Force Participation Rate"] = web.DataReader("CIVPART", "fred",start, end).resample("M").first() / 100
dfDict["Monthly"]["Labor Force (Nonfarm)"] = web.DataReader("PAYEMS", "fred",start, end).resample("M").first()

dfDict["Quarterly"] = web.DataReader("GDPC1", "fred", start, end).resample("Q").first()
dfDict["Quarterly"] = dfDict["Quarterly"].rename(columns = {"GDPC1":"Real GDP"})
dfDict["Quarterly"]["Nominal GDP"] = web.DataReader("GDP", "fred", start, end).resample("Q").first()
dfDict["Quarterly"]["GDP Deflator"] = web.DataReader("GDPDEF", "fred", start, end).resample("Q").first()



for key in dfDict["Monthly"]:
    dfDict["Quarterly"][key]= dfDict["Monthly"][key].resample("Q").first()
#    dfDict["Yearly"][key] = dfDict["Monthly"][key].resample("A").first()

#for key in dfDict["Quarterly"]:
#    dfDict["Yearly"][key] = dfDict["Quarterly"][key].resample("A").first()
#dfDict["Yearly"].dropna()

dfDict["Year Over Year Rate (Monthly)"] = web.DataReader("CIVPART", "fred", start, end).resample("M").first()
dfDict["Year Over Year Rate (Monthly)"] = dfDict["Year Over Year Rate (Monthly)"].rename(columns = {"CIVPART":"Labor Force Participation Rate"})
dfDict["Year Over Year Rate (Quarterly)"] = web.DataReader("GDPC1", "fred", start, end).resample("Q").first()
dfDict["Year Over Year Rate (Quarterly)"] = dfDict["Year Over Year Rate (Quarterly)"].rename(columns = {"GDPC1":"Real GDP"})

for key in dfDict["Monthly"]:
    if "Rate" not in key:
        dfDict["Year Over Year Rate (Monthly)"][key] = dfDict["Quarterly"][key].pct_change(periods=12)
    else:
        print("Rate is in this key:", key)
        dfDict["Year Over Year Rate (Monthly)"][key] = dfDict["Quarterly"][key]

for key in dfDict["Quarterly"]:
    if "Rate" not in key:
        dfDict["Year Over Year Rate (Quarterly)"][key] = dfDict["Quarterly"][key].pct_change(periods=4)
    else:
        print("Rate is in this key:", key)
        dfDict["Year Over Year Rate (Quarterly)"][key] = dfDict["Quarterly"][key]
dfDict["Year Over Year Rate (Monthly)"] = dfDict["Year Over Year Rate (Monthly)"].dropna()
dfDict["Year Over Year Rate (Quarterly)"] = dfDict["Year Over Year Rate (Quarterly)"].dropna()

for key in dfDict:
    print(dfDict[key])

namesDict = {}
namesDict[0] = ["Unemployment Rate", "Natural Rate of Unemployment"]
namesDict[1] = ["Unemployment Rate", "Labor Force Participation Rate"]
namesDict[2] = ["Real GDP", "Unemployment Rate"]
namesDict[3] = ["Nominal GDP", "Unemployment Rate"]
namesDict[4] = ["GDP Deflator", "Unemployment Rate"]

for dataType in dfDict:
#    if "Year" in dataType and "Monthly" in dataType:
    for key in namesDict: 
        names = namesDict[key]
        if names[0] in dfDict[dataType].keys() and names[1] in dfDict[dataType].keys():
            plotDF(dfDict[dataType], names,pp, title=dataType, secondary_y=None, logy=False, legend=True, dataType=dataType, start=start,end=end)
            plotDF(dfDict[dataType], names,pp, title=dataType, secondary_y=names[1], logy=False, legend=True, dataType=dataType, start=start,end=end)
            scatterPlot(dfDict[dataType], names[0],names[1], pp, dataType = dataType, title=dataType)
pp.close()
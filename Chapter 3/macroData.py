import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like

import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

def plotDF(df, names,pp, title="", secondary_y=None, logy=False, legend=False, dataType="",
           start=None,end=None):
    plt.rcParams['axes.ymargin'] = 0
    plt.rcParams['axes.xmargin'] = 0
    fig = df[names][start:end].plot.line(logy=logy, secondary_y=secondary_y, legend=legend,figsize=(10,6), color=['k', 'C3','C0'], fontsize=14).get_figure()
    if "Diff" in dataType: plt.axhline(0, color="k", ls="--", linewidth=1)
    plt.xticks(rotation=90)
    plt.xlabel(df.index.name, fontsize=18)
    if title == "":
        if len(names) < 2:
            plt.title(names[0], fontsize=24)
    else:
        plt.title(title)
    plt.gcf()
    if start == None:start=""
    if end == None: end = ""
    plt.savefig(dataType + " " + str(start).replace(":","") + "-" + str(end).replace(":","")+ " " +
                str(names).replace('[',' ').replace(']',' '+'.png'),bbox_inches="tight")
    plt.show()
    pp.savefig(fig)




    
pp = PdfPages("Macro Data.pdf")
start = datetime.datetime(2000, 1, 1)
end = datetime.datetime(2018, 6, 1)
##annual data
dfDict = {}
###
dfDict["Data"]  = web.DataReader("IOER", "fred", start, end)#.resample("Q").first()
dfDict["Data"]["Excess Reserves"] = web.DataReader("EXCSRESNS", "fred", start, end)
dfDict["Data"]["Base Money"] = web.DataReader("AMBNS", "fred",start, end).resample("Q").first()

dfDict["Data"] = web.DataReader("GDP", "fred", start, end).resample("Q").first()
dfDict["Data"] = dfDict["Data"].rename(columns = {"GDP":"Gross Domestic Product"})
dfDict["Data"]["Real Gross Domestic Product"] = web.DataReader("GDPC1", "fred", start, end).resample("Q").first()
dfDict["Data"]["Real GDP Per Capita"] = web.DataReader("A939RX0Q048SBEA","fred", start, end).resample("Q").first()
#dfDict["Data"]["GDP Deflator"] = web.DataReader("GDPDEF", "fred", start, end).resample("Q").first()
##dfDict["Data"] = web.DataReader("CPIAUCSL", "fred", start, end).resample("Q").first()
##dfDict["Data"] = dfDict["Data"].rename(columns = {"CPIAUCSL":"Consumer Price Index"})
#
#dfDict["Data"]["Consumer Price Index"] = web.DataReader("CPIAUCSL", "fred", start, end).resample("Q").first()
#
dfDict["Data"]["Base Money"] = web.DataReader("AMBNS", "fred",start, end).resample("Q").first()
#
dfDict["Data"] ["IOER"] = web.DataReader("IOER", "fred", start, end).resample("Q").first()
dfDict["Data"]["Excess Reserves"] = web.DataReader("EXCSRESNS", "fred", start, end).resample("Q").first()
dfDict["Data"]["Base Money"] = web.DataReader("AMBNS", "fred",start, end).resample("Q").first()
dfDict["Data"]["Base Money"] = dfDict["Data"]["Base Money"] * 1000
dfDict["Data"]["Effective Base"] = dfDict["Data"]["Base Money"] - dfDict["Data"]["Excess Reserves"]
dfDict["Data"]["Total Return on ER"] = dfDict["Data"]["IOER"] * dfDict["Data"]["Excess Reserves"]
#dfDict["Data"]["% Change in Base from IOER (annual)"] = dfDict["Data"]["Total Return on ER"] / dfDict["Data"]["Base Money"]
#dfDict["Data"]["% Change in Effective Base from IOER (annual)"] = dfDict["Data"]["Total Return on ER"] / (dfDict["Data"]["Base Money"] - dfDict["Data"]["Excess Reserves"])
dfDict["Data"]["Inflation Rate"] = ((np.log(web.DataReader("CPALTT01USM661S", "fred",start, end).resample("Q").first()).diff() + 1) ** 12 - 1) * 100

##dfDict["Data"]["Trade Weighted U.S. Dollar Index"] = web.DataReader("DTWEXM", "fred",start, end).resample("Q").first()
#
dfDict["Data"].index.names=['Year']

#dfDict["Data"]['Real GDP 10 Year Moving Average'] = dfDict["Data"]["Real Gross Domestic Product"].rolling(window=10).mean()
#dfDict["Data"]['Real GDP Per Capita 10 Year Moving Average'] = dfDict["Data"]["Real GDP Per Capita"].rolling(window=10).mean()

dfDict["Logged Values"]=np.log(dfDict["Data"])
dfDict["Logged Diff"] = dfDict["Logged Values"].diff()



#for key in dfDict:    
#    dfDict[key]["CPI - GDP Deflator"] = dfDict[key]["Consumer Price Index"] -\
#    dfDict[key]["GDP Deflator"]
#
##      start, end).resample("Q").first().values
##monthly data
##df["Reserves Excluding Gold"] = web.DataReader("TRESEGUSM052N", "fred", 
##        start, end).resample("Q").first().values#.resample("3M").first()
#
##df["M3 for the United States"] = web.DataReader("MABMM301USM189S", "fred",
##      start, end).resample("Q").first().values#.resample("3M").first()
#
##df["Industrial Production: Mining: Gold ore and silver ore mining"] = web.DataReader("IPG21222S", "fred", 
##      start, end).resample("Q").first().values#.resample("3M").first()
#
##df["Producer Price Index"] = web.DataReader("PCU2122221222", "fred",
##      start, end).resample("Q").first().values#.resample("3M").first()
#start = datetime.datetime(1975, 1, 1)
#money = web.DataReader("M1", "fred").resample("Q").first() 
#money["M2"] = web.DataReader("M2", "fred").resample("Q").first()#,
#
countDict = {}
#start=None
#end=None#"2008"
#
for key in dfDict:
    for key1 in dfDict["Data"]:
        for key2 in dfDict["Data"]:
            countDict[key1+key2]=False  
    df = dfDict[key]
    for key1 in dfDict["Data"]:
#        if "Logged" in key:
        plotDF(df, [key1], title=key1, pp=pp, dataType=key,start = start, end = end)
#        else:
#            plotDF(df, [key1], title=key1, logy=True, pp=pp)
            
        for key2 in dfDict["Data"]:    
            if key1 != key2:
                if countDict[key1+key2]==False:
#                    if "Logged" in key:
                    plotDF(df, [key1, key2], title="", secondary_y=key2, legend=True, pp=pp, dataType=key,start = start, end = end)
                    
#                    else:
#                        plotDF(df, [key1, key2], title="", logy=True, legend=True, pp=pp)
                
                    countDict[key1+key2]=True
                    countDict[key2+key1]=True
##for key1 in dfDict:
##    if "Diff" not in key1:
##        for key2 in dfDict:
##            if "Diff" not in key2:
##                for name in dfDict[key1]:
##                    dictNames = [key1, key2]
##                    df = pd.DataFrame(dfDict[key1][name], dfDict[key2][name])
##                    print(df)
##                    plotDF(df, [name], pp = pp, title=name )
#     
#                
##        plotDF(df, ["Real GDP"],"Real Gross Domestic Product", logy=True)
##        plotDF(df, ["GDP","Real GDP"],"", logy=True)
##        plotDF(df, ["Base Money"],"Base Money", logy=True)
##        
##        plotDF(df, ["CPI"],"Base Money", logy=True)
#


#
#
#startYear = ["1952-12-31",
#         "1960-12-31",
#         "1968-12-31",
#         "1976-12-31",
#         "1980-12-31",
#         "1988-12-31",
#         "1992-12-31",
#         "2000-12-31",
#         "2008-12-31",
#         "2016-12-31"]
#endYear = ["1960-12-31",
#           "1968-12-31",
#           "1976-12-31",
#           "1980-12-31",
#           "1988-12-31",
#           "1992-12-31",
#           "2000-12-31",
#           "2008-12-31",
#           "2016-12-31",
#           "2018-06-30"]
#presidents =["Eisenhower",
#             "Kennedy / Johnson",
#             "Nixon / Ford",
#             "Carter",
#             "Reagan",
#             "H W Bush",
#             "Clinton",
#             "G W Bush",
#             "Obama",
#             "Trump"]
##
###FV = P *e**(r*t)
###np.ln(FV/P) = r*t
#continuouslycompoundedGrowthRate = {}
#continuouslycompoundedPerCapitaGrowthRate = {} 
#
#for i in range(len(endYear)):
#    start = startYear[i]
#    end = endYear[i]
#    president = presidents[i]
#    n = 4
#    t = int(end[:4]) - int(start[:4])
#    if president == "Trump":
#        t = 1.5
##        n = 6
#    P = dfDict["Data"]["Real Gross Domestic Product"][start]
#    FV = dfDict["Data"]["Real Gross Domestic Product"][end]
#    r = np.log(FV/P)/t 
#    continuouslycompoundedGrowthRate[presidents[i]] = [r]
#
#for i in range(len(endYear)):
#    start = startYear[i]
#    end = endYear[i]
#    t = int(end[:4]) - int(start[:4])
#    P = dfDict["Data"]["Real GDP Per Capita"][start]
#    FV = dfDict["Data"]["Real GDP Per Capita"][end]
#    r = np.log(FV/P)/t 
#    continuouslycompoundedPerCapitaGrowthRate[presidents[i]] = [r]
#
#""" GDP Growth Rate DataFrame """
#plt.rcParams.update({'font.size': 22})
#
#continuouslycompoundedGrowthRateDF = pd.DataFrame(continuouslycompoundedGrowthRate)
#continuouslycompoundedPerCapitaGrowthRateDF = pd.DataFrame(continuouslycompoundedPerCapitaGrowthRate)
#
##for i in range(len(endYear)):
#for key in continuouslycompoundedGrowthRateDF :
#    continuouslycompoundedGrowthRateDF[key] = continuouslycompoundedGrowthRateDF[key][0]
#    continuouslycompoundedPerCapitaGrowthRateDF[key] = continuouslycompoundedPerCapitaGrowthRateDF[key][0]
#    
#continuouslycompoundedGrowthRateDF =continuouslycompoundedGrowthRateDF.T
#continuouslycompoundedPerCapitaGrowthRateDF =continuouslycompoundedPerCapitaGrowthRateDF.T
#continuouslycompoundedGrowthRateDF[1] = continuouslycompoundedPerCapitaGrowthRateDF
##
#continuouslycompoundedGrowthRateDF = continuouslycompoundedGrowthRateDF.rename(columns = {continuouslycompoundedGrowthRateDF.columns[0]:"RGDP Growth Rate"})
#continuouslycompoundedGrowthRateDF = continuouslycompoundedGrowthRateDF.rename(columns = {continuouslycompoundedGrowthRateDF.columns[1]:"RGDP Per Capita Growth Rate"})
#continuouslycompoundedGrowthRateDF.index.names = ['President']
#
##plt.subplot(2,2,1)
#
#continuouslycompoundedGrowthRateDF.plot.bar(legend = False, subplots=True,  layout = (1,2),figsize = (25, 10), colors = [ "teal","C0"])#, sharex = False, sharey = True, )
#plt.show()
#plt.savefig('Real GDP Growth Rates by President.png',bbox_inches="tight")
##pp.savefig(fig)
#
##""" GDP Per Capita Growth Rate DataFrame """
##
##continuouslycompoundedPerCapitaGrowthRateDF =continuouslycompoundedPerCapitaGrowthRateDF.T
##
##continuouslycompoundedPerCapitaGrowthRateDF.index.names = ['President']
###plt.subplot(2,2,2)
##
##continuouslycompoundedPerCapitaGrowthRateDF.plot.bar()#.get_figure()
##plt.show()
##plt.savefig('Real GDP Per Capita Growth Rate by President.png',bbox_inches="tight")
##pp.savefig(fig)

pp.close()

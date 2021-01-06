#chapter5.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
""" Never perform the same operation twice 
    if you can avoid it """

def findIntersect(df):
    i = 0
    for row in df.iterrows():
        i+=1
    #    print(row[1][1], row[1][2])
        val1 = round(row[1][1],2)
        val2 = round(row[1][2],2)
        if val1 == val2 and val1 != 0:
            intersecty = val1
            intersectx = i
            return intersecty, intersectx


A = 1.7
s= .4
s1 = .55
dataDict = {}
dataDictA = {}
dataDict["Capital"] = []
dataDict["Labor"]= []

dataDictA["Capital"] = []
dataDictA["Labor"] = []

for i in range(1001):
    num = i ** .5
    dataDict["Capital"].append(num)
    dataDict["Labor"].append(num)
    dataDictA["Capital"].append(A * num)
    dataDictA["Labor"].append(A * num)
df = pd.DataFrame(dataDict)
dfA = pd.DataFrame(dataDictA)
plt.rcParams['axes.ymargin'] = 0
plt.rcParams['axes.xmargin'] = 0

plt.rcParams.update({'font.size': 17})

for key in df:
    fig, ax1 = plt.subplots(figsize=(10,6))
    df[key].plot.line(ax=ax1)
    for i in range(3,5):
        val = 5 ** i 
        plt.plot((val,val), (df[key][val],df[key][0]), ls = "--", color = "C7", linewidth = 1)
        plt.plot((0,val), (df[key][val],df[key][val]), ls = "--", color = "C7", linewidth = 1) 
        plt.text(val + 20 , df[key][val] - 1.5,  "(" + str(round(val)) + " , " +\
                 str(round(df[key][val],2)) + ")")
    ax1.set_ylabel(r"$Total$ $Output$")
    ax1.set_xlabel("\n" + r"$Quantity$ $of$ $%s$" % key)
    plt.title(key)
    plt.show()
    plt.close()

for key in df:
    fig, ax1 = plt.subplots(figsize=(10,6))
    df[key].plot.line(ax=ax1)
    dfA[key].plot.line(ax=ax1)
    for i in range(4,5):
        val = 5 ** i 
        plt.plot((val,val), (dfA[key][val],dfA[key][0]), ls = "--", color = "C7", linewidth = 1)
        plt.plot((0,val), (df[key][val],df[key][val]), ls = "--", color = "C7", linewidth = 1) 
        plt.plot((0,val), (dfA[key][val],dfA[key][val]), ls = "--", color = "C7", linewidth = 1) 

        plt.text(val + 20 , df[key][val] - 3.75,  "(" + str(round(val)) + " , " +\
                 str(round(df[key][val],2)) + ")")
        plt.text(val + 20 , dfA[key][val] - 3.75,  "(" + str(round(val)) + " , " +\
                 str(round(dfA[key][val],2)) + ")")

    ax1.set_ylabel(r"$Total$ $Output$")
    ax1.set_xlabel("\n" + r"$Quantity$ $of$ $%s$" % key)
    plt.title(key)
    plt.show()
    plt.close()

""" Solow """
solowDict = {}
solowDictA = {}

solowDict["Income"] = []
solowDict["Savings"] = []
solowDict["New Savings"] = []

solowDict["Depreciation"] = []

solowDictA["Income"] = []
solowDictA["Savings"] = []
solowDictA["Depreciation"] = []

for i in range(10001):
    num = i ** .5
    solowDict["Income"].append(num)
    solowDict["Savings"].append(s * num)
    solowDict["New Savings"].append(s1 * num)
    solowDict["Depreciation"].append(i * .01)
    
    
    solowDictA["Income"].append(A * num)
    solowDictA["Savings"].append(A * s * num)
    solowDictA["Depreciation"].append(i * .01)

df = pd.DataFrame(solowDict)
dfA = pd.DataFrame(solowDictA)
intersecty = None
intersectx = None
i=0


intersecty, intersectx = findIntersect(df[["Income", "Savings", "Depreciation"]])
print(intersecty)

i=0


newIntersecty, newIntersectx = findIntersect(dfA) 

        
#    print(row["Savings"], row["Depreciation"])
fig, ax1 = plt.subplots(figsize=(10,6))
df[["Income", "Savings"]].plot.line(ax=ax1,color=["C0","C2","C3"])
plt.setp(ax1.get_xticklabels(), visible=False)
plt.setp(ax1.get_yticklabels(), visible=False)

#    for i in range(3,5):
#        val = 8 ** i 
#        plt.plot((val,val), (df[key][val],df[key][0]), ls = "--", color = "C7")
#        plt.plot((0,val), (df[key][val],df[key][val]), ls = "--", color = "C7") 
#        plt.text(val + 20 , df[key][val] - 1.5,  "(" + str(round(val)) + " , " +\
#                 str(round(df[key][val],2)) + ")")
ax1.set_ylabel(r"$Real$ $Income$ $Per$ $Capita$")
ax1.set_xlabel(r"$Effective$ $Capital$")
y = plt.text(-400, 50, "$y$", fontsize=24)
kl = plt.text(10000, -10, "$k$", fontsize=24)
plt.title("Solow Model")
plt.show()
plt.close()
    

fig, ax1 = plt.subplots(figsize=(10,6))
df[["Income", "Savings"]].plot.line(ax=ax1,color=["C0","C2","C3"])
plt.setp(ax1.get_xticklabels(), visible=False)
plt.setp(ax1.get_yticklabels(), visible=False)

#    for i in range(3,5):
#        val = 8 ** i 
#        plt.plot((val,val), (df[key][val],df[key][0]), ls = "--", color = "C7")
#        plt.plot((0,val), (df[key][val],df[key][val]), ls = "--", color = "C7") 
#        plt.text(val + 20 , df[key][val] - 1.5,  "(" + str(round(val)) + " , " +\
#                 str(round(df[key][val],2)) + ")")
ax1.set_ylabel(r"$Real$ $Income$ $Per$ $Capita$")
ax1.set_xlabel(r"$Effective$ $Capital$")
y = plt.text(-400, 50, "$y$", fontsize=24)
kl = plt.text(10000, -10, "$k$", fontsize=24)
plt.title("Solow Model")
plt.show()
plt.close()
    


newSavingsIntersecty, newSavingsIntersectx = findIntersect(df[["Income", "New Savings", "Depreciation"]])




fig, ax1 = plt.subplots(figsize=(10,6))
df[["Income","Savings","Depreciation"]].plot.line(ax=ax1, color=["C0","C2","C3"])
plt.setp(ax1.get_xticklabels(), visible=False)
plt.setp(ax1.get_yticklabels(), visible=False)
plt.xlim(xmax=7000)
#plt.ylim(ymax=150)

#    for i in range(3,5):
#        val = 8 ** i 
plt.plot((intersectx,intersectx), (df["Income"][intersectx],0), ls = "--", color = "C7", linewidth = 1)
plt.plot((0,intersectx), (intersecty,intersecty), ls = "--", color = "C7", linewidth = 1)
plt.plot((0,intersectx), (df["Income"][intersectx], df["Income"][intersectx]), ls = "--", color = "C7", linewidth = 1)


#plt.text(intersectx + 25 , intersecty - 5,  "(" + str(round(intersectx)) + " , " +\
#         str(int(round(intersecty))) + ")")\
plt.text(intersectx + 25 , intersecty - 9,  "^Steady State\nLevel of Savings", fontsize = 14)
plt.text(intersectx + 25 , intersecty + 16,  "^Steady State\nLevel of Income", fontsize = 14)
plt.text(-325, df["Income"][intersectx], "$y_0^*$")
plt.text(-450, intersecty, "$sy_0^*$")
plt.text(intersectx - 90, -7, "$k_0^*$")

#         str(int(round(intersecty))) + ")")
#plt.plot((0,val), (df[key][val],df[key][val]), ls = "--", color = "C7") 
#        plt.text(val + 20 , df[key][val] - 1.5,  "(" + str(round(val)) + " , " +\
#                 str(round(df[key][val],2)) + ")")
#ax1.set_ylabel(r"$Real$ $Income$ $Per$ $Capita$")
#ax1.set_xlabel(r"$Effective$ $Capital$")
y = plt.text(-400, 100, "$y$", fontsize=24)
kl = plt.text(7000, -10, "$k$", fontsize=24)
plt.title("Solow Model")
plt.show()
plt.close()





fig, ax1 = plt.subplots(figsize=(10,6))
df.plot.line(ax=ax1, color=["C0","C2","C2", "C3"])
plt.setp(ax1.get_xticklabels(), visible=False)
plt.setp(ax1.get_yticklabels(), visible=False)
plt.xlim(xmax=7000)
#plt.ylim(ymax=150)

#    for i in range(3,5):
#        val = 8 ** i 
plt.plot((intersectx,intersectx), (df["Income"][intersectx],0), ls = "--", color = "C7", linewidth = 1)
plt.plot((0,intersectx), (intersecty,intersecty), ls = "--", color = "C7", linewidth = 1)
plt.plot((0,intersectx), (df["Income"][intersectx], df["Income"][intersectx]), ls = "--", color = "C7", linewidth = 1)

plt.plot((newSavingsIntersectx,newSavingsIntersectx), (df["Income"][newSavingsIntersectx],0), ls = "--", color = "C7", linewidth = 1)
plt.plot((0,newSavingsIntersectx), (newSavingsIntersecty,newSavingsIntersecty), ls = "--", color = "C7", linewidth = 1)
plt.plot((0,newSavingsIntersectx), (df["Income"][newSavingsIntersectx], df["Income"][newSavingsIntersectx]), ls = "--", color = "C7", linewidth = 1)



#plt.text(intersectx + 25 , intersecty - 5,  "(" + str(round(intersectx)) + " , " +\
#         str(int(round(intersecty))) + ")")\
#plt.text(intersectx + 25 , intersecty - 9,  "^Steady State\nLevel of Savings", fontsize = 14)
#plt.text(intersectx + 25 , intersecty + 16,  "^Steady State\nLevel of Income", fontsize = 14)
plt.text(-325, df["Income"][intersectx], "$y_0^*$")
plt.text(-450, intersecty, "$sy_0^*$")
plt.text(intersectx - 90, -7, "$k_0^*$")

plt.text(-325, df["Income"][newSavingsIntersectx], "$y_0^*$")
plt.text(-450, newSavingsIntersecty, "$sy_1^*$")
plt.text(newSavingsIntersectx - 90, -7, "$k_1^*$")

#         str(int(round(intersecty))) + ")")
#plt.plot((0,val), (df[key][val],df[key][val]), ls = "--", color = "C7") 
#        plt.text(val + 20 , df[key][val] - 1.5,  "(" + str(round(val)) + " , " +\
#                 str(round(df[key][val],2)) + ")")
#ax1.set_ylabel(r"$Real$ $Income$ $Per$ $Capita$")
#ax1.set_xlabel(r"$Effective$ $Capital$")
y = plt.text(-400, 100, "$y$", fontsize=24)
kl = plt.text(7000, -10, "$k$", fontsize=24)
plt.title("Solow Model")
plt.show()
plt.close()





fig, ax1 = plt.subplots(figsize=(10,6))
dfA.plot.line(ax=ax1, color=["C0","C2","C3"], legend = False)
df[["Income", "Savings"]].plot.line(ax=ax1, color=["C0","C2","C3"], legend = False)

plt.ylim(ymax=150)

plt.setp(ax1.get_xticklabels(), visible=False)
plt.setp(ax1.get_yticklabels(), visible=False)
plt.xlim(xmax=7000)

#    for i in range(3,5):
#        val = 8 ** i 
plt.plot((intersectx,intersectx), (df["Income"][intersectx],0), ls = "--", color = "C7", linewidth = 1)
plt.plot((0,intersectx), (intersecty,intersecty), ls = "--", color = "C7", linewidth = 1)
plt.plot((0,intersectx), (df["Income"][intersectx], df["Income"][intersectx]), ls = "--", color = "C7", linewidth = 1)

plt.plot((newIntersectx,newIntersectx), (dfA["Income"][newIntersectx],0), ls = "--", color = "C7", linewidth = 1)
plt.plot((0,newIntersectx), (newIntersecty,newIntersecty), ls = "--", color = "C7", linewidth = 1)
plt.plot((0,newIntersectx), (dfA["Income"][newIntersectx], dfA["Income"][newIntersectx]), ls = "--", color = "C7", linewidth = 1)


#plt.text(intersectx + 25 , intersecty - 5,  "(" + str(round(intersectx)) + " , " +\
#         str(int(round(intersecty))) + ")")\
plt.text(intersectx + 25 , intersecty + 19,  "^Old", fontsize = 14)
plt.text(-325, df["Income"][intersectx], "$y_0$")
plt.text(-450, intersecty, "$sy_0$")
plt.text(intersectx - 90, -7, "$k_0$")

plt.text(newIntersectx + 25 , newIntersecty + 64,  "^New", fontsize = 14)
plt.text(-325, dfA["Income"][newIntersectx], "$y_1$")
plt.text(-450, newIntersecty, "$sy_1$")
plt.text(newIntersectx - 90, -7, "$k_1$")

#         str(int(round(intersecty))) + ")")
#plt.plot((0,val), (dfA[key][val],dfA[key][val]), ls = "--", color = "C7") 
#        plt.text(val + 20 , dfA[key][val] - 1.5,  "(" + str(round(val)) + " , " +\
#                 str(round(dfA[key][val],2)) + ")")
#ax1.set_ylabel(r"$Real$ $Income$ $Per$ $Capita$")
#ax1.set_xlabel(r"$Effective$ $Capital$")
y = plt.text(-400, 150, "$y$", fontsize=24)
kl = plt.text(7000, -10, "$k$", fontsize=24)
plt.title("Solow Model")
plt.show()
plt.close()




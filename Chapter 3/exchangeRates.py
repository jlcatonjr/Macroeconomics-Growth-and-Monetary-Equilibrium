#macroDataTutorial.py
""" dataframes"""
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import matplotlib.pyplot as plt

""" scrape data from online """

""" install pandas_datareader with:
    window search: "command" will open command prompt
    conda install -c anaconda pandas-datareader
    """
import pandas_datareader.data as web

""" cite the start and end dates for data """
import datetime
plt.rcParams['axes.xmargin'] = 0

start = datetime.datetime(2000, 1, 1)
end = datetime.datetime(2018, 6, 1)
x = web.DataReader("EXVZUS", "fred", start, end).resample("A").first()
x = x.rename(columns = {"EXVZUS":"Bolivar:US Dollar"})
x["Inflation in Venezuela"] = web.DataReader("FPCPITOTLZGVEN", "fred", start, end).resample("A").first()

#x["Real GDP"] = web.DataReader("GDPC1", "fred", start, end)
#
#
#""" hash sign # comments out the text"""
## ***********  #hash sign comment out the text **********************
#names = ["AMBNS",
#         "GDPDEF",
#         "CPIAUCSL"]
#for name in names:
#    print(name)
#    x[name] = web.DataReader(name, "fred", start, end)

#x["GDP Deflator"] = x["GDP"] / x["Real GDP"] * 100
#x= x.rename(columns={"AMBNS":"Base Money"})
#print(x)
#
#x.to_csv("FRED Data.csv")
##datetime.datetime()
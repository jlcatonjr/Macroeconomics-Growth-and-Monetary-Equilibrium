import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import numpy as np
import os
import copy
from matplotlib.backends.backend_pdf import PdfPages
from statsmodels.tsa.api import VAR, DynamicVAR

def gather_data(data_codes, start, end = datetime.datetime.today(), freq = "A"):
    i = 0
    # dct.items() calls key and value that key points to
    for key, val in data_codes.items():
        if i == 0:
            # Create dataframe for first variable, then rename column
            df = web.DataReader(val, "fred", start, end).resample(freq).first()
            df.rename(columns = {val:key}, inplace = True) 
            i = None
        else:
            # If dataframe already exists, add new column
            df[key] = web.DataReader(val, "fred", start, end).resample(freq).first()
            
    return df
    
def plot_lines(df, plot_vars, linewidth = 1, logy = False, figsize = (40,20), 
    secondary_y = None, pp = None):
    
    fig, ax = plt.subplots(figsize = figsize)
    
    legend_scale = 20 / figsize[1]
    # If no secondary_y (axis), plot all variables at once
    if secondary_y == None:
        df[plot_vars].plot.line(linewidth = linewidth, logy = logy, ax = ax)
        ax.legend(bbox_to_anchor=(0, 1.035 + .045 * len(plot_vars) * legend_scale), 
                  loc=2)
    # Otherwise, create a new axis and plot each variable individually
    else:
        ax2 = ax.twinx()
        for var in plot_vars:
            if var == secondary_y: 
                df[var].plot.line(linewidth = linewidth, logy = logy, ax = ax2)
            else:
                df[var].plot.line(linewidth = linewidth, logy = logy, ax = ax)
        # If there are two axes, then gather lines from each axis
        lines = ax.get_lines() + ax2.get_lines()
        # then gather the label from each line
        labels = [l.get_label() for l in lines]
        # and use the lines and labels to create the legend
        ax.legend(lines, labels, bbox_to_anchor=(0, 
                1.04 + .045 * len(plot_vars) * legend_scale), loc=2)
    # Turn the text on the x-axis so that it reads vertically
    ax.tick_params(axis='x', rotation=90)
    # Get rid of tick lines perpendicular to the axis for aesthetic
    ax.tick_params('both', length=0, which='both')
    # save image if PdfPages object was passed
    if pp != None: pp.savefig(fig, bbox_inches = "tight")

def plot_scatter(df, plot_vars, s = 100, figsize = (40, 20), pp = None):
    # Create plot for every unique pair of variables
    for var1 in plot_vars:
        for var2 in plot_vars:
            if var1 != var2:
                fig, ax = plt.subplots(figsize = figsize)
                # Create list of years from index
                # Year will be represented by color
                years = [int(str(ind)[:4]) for ind in df.index]
                df.plot.scatter(x = var1, y = var2, s = s, ax = ax, c = years,
                                cmap = "viridis")
                # Save image if PdfPages object was passed
                if pp != None: pp.savefig(fig, bbox_inches = "tight")

pp = PdfPages("Macro Measures " + str(datetime.datetime.today())[:10] + ".pdf")
plt.rcParams.update({'font.size': 32})
data_codes  = {"Nominal GDP":"GDP",
               "Price Level":"GDPDEF",
               "Population":"B230RC0A052NBEA",
               "Base Money": "BOGMBASEW",
               "Base Money in Circulation":"MBCURRCIRW",
               "M1":"M1",
               "M2":"M2",
               "Total Assets": "WALCL",
               }

start = datetime.datetime(1975, 1, 1)
end = datetime.datetime(2019, 9, 30)

if "data_gathered" not in locals():    
    df = gather_data(data_codes, start, 
          end = datetime.datetime.today(), freq = "Q")
    df["Population"] = df["Population"] / 10 ** 3
    df["Price Level"] = df["Price Level"].div(df["Price Level"].loc[end])
    df["Nominal GDP"] = df["Nominal GDP"] * 10 ** 3
    df["Real GDP"] = df["Nominal GDP"].div(df["Price Level"])
    df["Real GDP Per Capita"] = df["Real GDP"].div(df["Population"])
    df["Base Money Velocity"] = df["Nominal GDP"].div(df["Base Money"])
    df["Base Money Circ. Velocity"] = df["Nominal GDP"].div(df["Base Money in Circulation"])
    df["Percent Base in Circ."] = df["Base Money in Circulation"] / df["Base Money"]
    df["Assets Less Base"] = df["Total Assets"].sub(df["Base Money"]) 
    df["Assets Less Base in Circ."] = df["Total Assets"].sub(df["Base Money in Circulation"]) 
    df["Base to Assets"] = df["Base Money"].div(df["Total Assets"])
    df["Base in Circ. to Assets"] = df["Base Money in Circulation"].div(df["Total Assets"])
    data_gathered = True

data_dict = {"Data":df, "Log":np.log(df), "Log Diff":np.log(df).diff()}
for key in data_dict:
    data_dict[key]["Percent Base in Circ."] = data_dict["Data"]["Percent Base in Circ."]
    data_dict[key]["Base in Circ. to Assets"] = data_dict["Data"]["Base in Circ. to Assets"]

for key, data in data_dict.items():
    plot_vars = ["Base Money Circ. Velocity", "Percent Base in Circ."]
    plot_lines(data, plot_vars, linewidth = 3, pp = pp,
               secondary_y = "Percent Base in Circ.") 
    plot_vars = ["Base Money Circ. Velocity", "Base in Circ. to Assets"]
    plot_lines(data, plot_vars, linewidth = 3, pp = pp,
               secondary_y = "Base in Circ. to Assets") 
    plot_vars = ["Base Money Circ. Velocity", "Base to Assets"]
    plot_lines(data, plot_vars, linewidth = 3, pp = pp,
               secondary_y = "Base to Assets") 
#    plot_scatter(df, plot_vars, pp = pp)
pp.close()
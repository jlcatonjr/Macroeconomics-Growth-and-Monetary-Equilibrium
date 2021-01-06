import pandas as pd

pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

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
                df[var].plot.line(linewidth = linewidth, logy = logy, ax = ax2, c = "C9",
                  label = var + " (right)")
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

def plot_scatter(df, plot_vars, s = 75, figsize = (40, 20), pp = None):
    # Create plot for every unique pair of variables
    for var1 in plot_vars:
        for var2 in plot_vars:
            if var1 != var2:
                fig, ax = plt.subplots(figsize = figsize)
                # Create list of years from index
                # Year will be represented by color
                df["Year"] = [int(str(ind)[:4]) for ind in df.index]
                df.plot.scatter(x = var1, y = var2, s = s, ax = ax, c = "Year",
                                cmap = "viridis")
                # Turn the text on the x-axis so that it reads vertically
                ax.tick_params(axis='x', rotation=90)
                # Get rid of tick lines perpendicular to the axis for aesthetic
                ax.tick_params('both', length=0, which='both')
                # save image if PdfPages object was passed
                if pp != None: pp.savefig(fig, bbox_inches = "tight")

# Create PDF that will hold visualizations
pp = PdfPages("Capital Measures " + str(datetime.datetime.today())[:10] + ".pdf")
# set default fontsize for text in plot
plt.rcParams.update({'font.size': 32})
# Choose data from FRED
# Keys will be used to name variable. Key points to FRED code
data_codes  = {"Capital Stock":"RKNANPUSA666NRUG",
               "Nominal GDP":"GDP",
               "Price Level":"GDPDEF",
               "Population":"B230RC0A052NBEA"}
# Select start and end dates
start = datetime.datetime(1950, 1, 1)
end = datetime.datetime(2019, 1, 31)

# Check if data has been gathered.
# If data needs to be gathered again, clear variables or restart kernel
if "data_gathered" not in locals():
    df = gather_data(data_codes, start, 
          end = datetime.datetime.today(), freq = "A")
    # After data is downloaded create new data and transform data
    # set population to millions        
    df["Population"] = df["Population"] / 10 ** 3
    # set NGDP to millions
    df["Nominal GDP"] = df["Nominal GDP"] * 10 ** 3
    # Make 2011 base year for price level to match capital stock values
    df["Price Level"] = df["Price Level"].div(df["Price Level"].loc["2011"].values[0])
    # Create RGDP using 2011 prices
    df["Real GDP"] = df["Nominal GDP"].div(df["Price Level"])
    # Use population as proxy for L
   # y = Y / L
    df["Real GDP Per Capita"] = df["Real GDP"].div(df["Population"])
    # k = K / L
    df["Effective Capital Stock"] = df["Capital Stock"].div(df["Population"])
    # Estimate Solow's A
    # y = Ak**.5
    # A = y / k ** .5
    df["Efficiency of Capital"] = df["Real GDP Per Capita"].div(df["Effective Capital Stock"] ** (1/2))
    data_gathered = True

####### Plot Variables #######
plot_vars = ["Effective Capital Stock"]
plot_lines(df, plot_vars, linewidth = 3, logy = True, pp = pp)
plot_vars = ["Efficiency of Capital", "Real GDP Per Capita"]
plot_lines(df, plot_vars, linewidth = 3, logy = True, 
           secondary_y = "Efficiency of Capital", pp = pp)

plot_scatter(df, plot_vars, pp = pp)

pp.close()
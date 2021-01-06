import pandas as pd
import numpy as np

scale = {}
scale["Constant Returns to Scale"] = np.arange(101)
scale["Decreasing Returns to Scale"] = [i ** .9 for i in range(101)]
scale["Increasing Returns to Scale"] = [i ** 1.1 for i in range(101)]
plt.rcParams.update({'font.size': 10})

scaleDF = pd.DataFrame(scale)
fig,ax = plt.subplots(figsize=(12,6))
scaleDF.plot.line(ax=ax)
ax.set_ylabel(r"$Income$", fontsize=24)
ax.set_xlabel(r"$Investment$", fontsize=24)
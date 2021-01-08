#%matplotlib notebook
import ipywidgets as ipw 
import numpy as np
import matplotlib.pyplot as plt

class livePlot(): 
    def __init__(self, demand_slope = -1, demand_y_int = 10**2, supply_slope = 1, supply_y_int = 0):
        self.fig, self.ax = plt.subplots(1, figsize = (8, 6))
        self.demand_slope = demand_slope  
        self.demand_y_int = demand_y_int 
        self.supply_slope = supply_slope 
        self.supply_y_int = supply_y_int 
        plt.rcParams["font.size"] = 20
        x_max = 100
        num_divisions = 1000
        self.ax.set_xlim(0, x_max)
        self.ax.set_ylim(0, self.demand_y_int)
        plt.xticks([])
        plt.yticks([])

        self.units = x_max / num_divisions
        self.x = np.linspace(0, x_max, num_divisions)

        self.demand, = self.ax.plot(self.x, self.demand_y_int + self.demand_slope * self.x, c = "C0")
        self.supply, = self.ax.plot(self.x, self.supply_y_int + self.supply_slope * self.x, c = "C0")


        x_intersect, y_intersect = self.get_intersect(self.demand, self.supply, line2_vert = False)
        x_intersect = x_intersect * self.units
        self.h_line_intersect, = self.ax.plot([0, x_intersect], [y_intersect, y_intersect],
                                      ls = "--", color = "k")
        self.v_line_intersect, = self.ax.plot([x_intersect,x_intersect],[0, y_intersect],
                                      ls = "--", color = "k")
        self.p_text = self.ax.text(-6, y_intersect - 1.2, "$p^*$")
        self.q_text = self.ax.text(x_intersect * .96, -6, "$q^*$")
        self.sd_text_x = int(1.6 * x_intersect)
        self.s_text = self.ax.text(self.sd_text_x,self.supply.get_ydata(orig=False)[int(self.sd_text_x / self.units)] - 5.5, "$S$")
        self.d_text = self.ax.text(self.sd_text_x,self.demand.get_ydata(orig=False)[int(self.sd_text_x / self.units)] + 2, "$D$")
    def interact(self):

        def update(demand, supply):
            def update_supply_and_demand():
                self.demand_y_int = demand
                self.supply_y_int = -supply
                self.demand.set_ydata(demand + self.demand_slope * self.x)
                self.supply.set_ydata(- supply + self.supply_slope * self.x)            
                x_intersect, y_intersect = self.get_intersect(self.demand, self.supply, line2_vert = False)
                x_intersect = x_intersect * self.units
                self.h_line_intersect.set_data([0, x_intersect], [y_intersect, y_intersect]) 
                self.v_line_intersect.set_data([x_intersect, x_intersect], [0, y_intersect])
                self.p_text.set_position((-11, y_intersect - 1.2))
                self.q_text.set_position((x_intersect * .96, -11))
                self.s_text.set_position((self.sd_text_x,self.supply.get_ydata(orig=False)[int(self.sd_text_x / self.units)] - 5.5))
                self.d_text.set_position((self.sd_text_x,self.demand.get_ydata(orig=False)[int(self.sd_text_x / self.units)] + 2 ))

                # self.ax.set_title(str(x_intersect)+ " " + str(y_intersect))
                
            update_supply_and_demand()

        self.widget = ipw.interact(update, 
                      demand = ipw.widgets.IntSlider(value=self.demand_y_int,
                        min=self.demand_y_int - 20,
                        max=self.demand_y_int + 20,
                        step = 1),
                    supply = ipw.widgets.IntSlider(value = self.supply_y_int,
                        min= self.supply_y_int - 20,
                        max = self.supply_y_int + 20,
                        step = 1))
        
    def get_intersect(self, line1, line2, line2_vert = False):
        if line2_vert == False:
            x = np.argwhere(np.diff(np.sign(line1.get_ydata(orig=False) - line2.get_ydata(orig=False)))).flatten()
            x = x[0]
        else:
            line1_data = line1.get_data()
            # set orig = False or else list reads as float
            line2_xdata = line2.get_xdata(orig=False)[0]
            dist = [np.abs(i - line2_xdata) for i in line1_data[0]]
            min_dist = min(dist)
            x = dist.index(min_dist)
        y = line1._y[x]
        return x, y
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.backends.backend_pdf import PdfPages

"""
Notes for future:
    You set up the basic elements of a curve, but not everything
    is truly automated. Need to:
        1. Automate Coordinates of S,D text
"""

# shift1 is demand shift, shift 2 is supply shift
def supplyAndDemandWithShifts(supply, demand, shift1=None, shift2=None, inc=1, ceiling = False, floor = False, name= "Loanable Funds", pp = PdfPages("Default.pdf")):
    pp = pp
    fig = plt.figure(dpi=128, figsize=(10,6))
    frame = plt.gca()                         
    plt.title(name, fontsize=24, ha='center')
    
 
    
    
    if shift1: 
        firstShift = selectShiftCurve(demand, supply, shift1,order=1)
    if shift2:
        secondShift = selectShiftCurve(demand, supply,shift1, shift2,order=2)
    i = 0

    if shift1 and shift2:
        xi,yi= findIntersection(supply, demand, inc)

        plotCurves(supply, demand, firstShift, secondShift, inc)
        placePrimaryText(supply, demand)
        p0, q0 = plotVertAndHorizLines(demand,supply,inc,i, "k--")
        i +=1

# Horizontal and Vertical Lines for First Shift        
        if shift1 == "Demand-Left" or shift1 == "Demand-Right":
            p1, q1 = plotVertAndHorizLines(firstShift, supply, inc,i, "k--")
        if shift1 == "Supply-Left" or shift1 == "Supply-Right":
            p1, q1 = plotVertAndHorizLines(firstShift, demand, inc,i, "k--")

        i += 1
        if (shift2 == "Demand-Left" or shift2 == "Demand-Right"):
            if (shift1 == "Demand-Left" or shift1 == "Demand-Right"):
                p2, q2 = plotVertAndHorizLines(secondShift, supply, inc,i, "k--", xi, yi)
                if shift1 != shift2:
                    p0.remove
                    q0.remove                    
            if (shift1 == "Supply-Left" or shift1 == "Supply-Right"):
                p2, q2 = plotVertAndHorizLines(secondShift, firstShift, inc, i, "k--", xi, yi)
                if (shift2 == "Demand-Left" and shift1 == "Supply-Right") or (shift2 == "Demand-Right" and shift1 == "Supply-Left") :
                    q0.remove
        if shift2 == "Supply-Left" or shift2 == "Supply-Right":
            if (shift1 == "Demand-Left" or shift1 == "Demand-Right"):
                print([secondShift, firstShift, inc,i, "k--", xi, yi])
                p2, q2 = plotVertAndHorizLines(secondShift, firstShift, inc,i, "k--", xi, yi)
                if (shift1 == "Demand-Left" and shift2 == "Supply-Right") or (shift1 == "Demand-Right" and shift2 == "Supply-Left") :
                    q0.remove
            if (shift1 == "Supply-Left" or shift1 == "Supply-Right"):
                p2, q2 = plotVertAndHorizLines(secondShift, demand, inc,i, "k--", xi, yi)
                if shift1 != shift2:
                    p0.remove
                    q0.remove                                    
    else:
        plotCurves(demand, supply)
        if demand is not None:
            if supply is not None:
                p0, q0 = plotVertAndHorizLines(demand,supply,inc,i, "k--")
            else:
                line="k--"
                plt.plot((3000, 3000), (0, demand[3000]), line, linewidth=1.5) 
                plt.plot((0,3000), (demand[3000], demand[3000]), line,linewidth=1.5)

                plt.plot((7000, 7000), (0, demand[7000]), line, linewidth=1.5) 
                plt.plot((0,7000), (demand[7000], demand[7000]), line,linewidth=1.5)
                plt.text(2900, -600, "$Q_0$", fontsize=22)
                plt.text(6900, -600, "$Q_1$", fontsize=22)
                plt.text(-350, demand[3000], "$P_0$", fontsize=22)
                plt.text(-350, demand[7000], "$P_1$", fontsize=22)

        else:
            line="k--"
            plt.plot((3000, 3000), (0, supply[3000]), line, linewidth=1.5) 
            plt.plot((0,3000), (supply[3000], supply[3000]), line,linewidth=1.5)
            plt.plot((7000, 7000), (0, supply[7000]), line, linewidth=1.5) 
            plt.plot((0,7000), (supply[7000], supply[7000]), line,linewidth=1.5)
            plt.text(2900, -600, "$Q_0$", fontsize=22)
            plt.text(6900, -600, "$Q_1$", fontsize=22)
            plt.text(-350, supply[3000], "$P_0$", fontsize=22)
            plt.text(-350, supply[7000], "$P_1$", fontsize=22)

    if shift1 and not shift2:
        plotCurves(supply, demand, firstShift, None, inc)
        placePrimaryText(supply, demand)
        p0, q0 = plotVertAndHorizLines(demand,supply,inc,i, "k--")

        # Horizontal and Vertical Lines for First Shift        
        i +=1
        if shift1 == "Demand-Left" or shift1 == "Demand-Right":
            p1, q1 = plotVertAndHorizLines(firstShift, supply, inc,i, "k--")
        if shift1 == "Supply-Left" or shift1 == "Supply-Right":
            p1, q1 = plotVertAndHorizLines(firstShift, demand, inc,i, "k--")


    if not shift1 and shift2:
        plotCurves(supply, demand, None, secondShift, inc)
        p0, q0 = plotVertAndHorizLines(demand,supply,inc,i, "k--")

        # Horizontal and Vertical Lines for First Shift        
        i +=1
        if shift1 == "Demand-Left" or shift1 == "Demand-Right":
            p1, q1 = plotVertAndHorizLines(firstShift, supply, inc,i, "k--")
        if shift1 == "Supply-Left" or shift1 == "Supply-Right":
            p1, q1 = plotVertAndHorizLines(firstShift, demand, inc,i, "k--")

  
    if shift1 == None and shift2 == None:
        if ceiling:
            ceilingLine = [2500 for i in range(10000)]
            p0, q0 = plotVertAndHorizLines(ceilingLine,supply,inc,"s", "k--", ceiling=ceiling)
            p0, q0 = plotVertAndHorizLines(ceilingLine,demand,inc,"d", "k--", ceiling=ceiling)
        if floor:
            floorLine = [7500 for i in range(10000)]
            p0, q0 = plotVertAndHorizLines(floorLine,supply,inc,"s", "k--", floor=floor)
            p0, q0 = plotVertAndHorizLines(floorLine,demand,inc,"d", "k--", floor=floor)
    placePrimaryText(supply, demand)
    placeShiftText(shift1, shift2)
    setupAxes(frame)
    pp.savefig(fig,bbox_inches="tight")
#    plt.close()
#    pp.close()

def placePrimaryText(supply, demand):
    #plt.text(x,y,text,fontsize)
    p = plt.text(-300, 10000, "$P$", fontsize=24)
    if supply is not None:
        s = plt.text(8200, 8800,"$S_0$", fontsize = 24)
    else:
        s = ""
    if demand is not None:
        d = plt.text(8200, 2000,"$D_0$", fontsize = 24)
    else:
        d=""
    q = plt.text(10000, -500, "$Q$", fontsize=24)
    return p , s , d , q 
    
def placeShiftText(shift1, shift2=None):    
    if shift1 == None:
        if (shift2):
            placeShiftText(shift2)
        else:            
            return
    
    if shift1 == "Demand-Left":
        plt.text(5500, 1600,"$D_1$", fontsize = 24)
    if shift1 == "Demand-Right":
        plt.text(8500, 4600,"$D_1$", fontsize = 24)
    if shift1 == "Supply-Left":
        plt.text(6600, 8800,"$S_1$", fontsize = 24)
    if shift1 == "Supply-Right":
        plt.text(8500, 7600,"$S_1$", fontsize = 24)

# safety check . . . 
    if shift1 and shift2:
        if shift2 == "Demand-Left":
            if shift1 == "Supply-Left" or shift1 == "Supply-Right":
                plt.text(6200, 1000,"$D_1$", fontsize = 24)
            if shift1 == "Demand-Left":    
                plt.text(4000, 1600,"$D_2$", fontsize = 24)
            if shift1 == "Demand-Right":
                plt.text(8200, 2000,"$D, D_2$", fontsize = 24) # same as initial
        if shift2 == "Demand-Right":
            if shift1 == "Supply-Left" or shift1 == "Supply-Right":
                plt.text(8500, 4600,"$D_1$", fontsize = 24)
            if shift1 == "Demand-Left":
                plt.text(8200, 2000,"$D, D_2$", fontsize = 24) # same as initial
            if shift1 == "Demand-Right":
                plt.text(9000, 5750,"$D_2$", fontsize = 24)
                

        if shift2 == "Supply-Left":
            if shift1 == "Demand-Left" or shift1 == "Demand-Right":
                plt.text(6600, 8800,"$S_1$", fontsize = 24)                
            if shift1 == "Supply-Left":
                plt.text(5100, 8800,"$S_2$", fontsize = 24)
            if shift1 == "Supply-Right":
                plt.text(7755, 8800,"$S, \ \ _2$", fontsize = 24) # same as initial

        if shift2 == "Supply-Right":
            if shift1 == "Demand-Left" or shift1 == "Demand-Right":
                plt.text(8500, 7600,"$S_1$", fontsize = 24)                
            if shift1 == "Supply-Left":
                plt.text(7755, 8800,"$S, \ \ _2$", fontsize = 24) # same as initial
            if shift1 == "Supply-Right":
                plt.text(9750, 6000,"$S_2$", fontsize = 24)        
        
    


def plotCurves(supply, demand, shift1=None, shift2=None,  inc=1):
    # plt.plot((x1,x2), (y1,y2), linestyle/color, linewidth)
    if supply is not None:
        plt.plot(supply, 'C0-', linewidth=3)
    if demand is not None:
        plt.plot(demand, 'C0-', linewidth=3)    
    try:
        if isinstance(shift1,np.ndarray):
            plt.plot(shift1, 'C3-', linewidth=3)
    except NameError:
        print("shift1 = None")    
#    if not np.all([shift2, supply]) and not np.all([shift2, demand]):
    try:
        if isinstance(shift2,np.ndarray):
            plt.plot(shift2, 'C3-', linewidth=3)
    except NameError:
        print("shift1 = None")    

def plotVertAndHorizLines(curve1,curve2,inc, i, line,xi = None, yi = None, ceiling=False, floor=False):
    x2,y2 = findIntersection(curve1, curve2, inc)

    plt.plot((x2, x2), (0, y2), line, linewidth=1.5) 
    plt.plot((0,x2), (y2, y2), line,linewidth=1.5)
    if i == 0:    
        p0 =plt.text(-400,y2, "$P_{0}$", fontsize=22)
        q0 = plt.text(x2 - 200, -550, "$Q_0$", fontsize=22)
        return p0, q0

    if i == 1:
        p1 = plt.text(-400,y2, "$P_{1}$", fontsize=22)
        q1 = plt.text(x2 - 200, -550, "$Q_1$", fontsize=22)
        return p1, q1
    if i == 2:
        if yi != y2:
            p2 = plt.text(-400,y2, "$P_{2}$", fontsize=22)
        else:
            p2 = plt.text(-1600,y2, "$P_{2}=$", fontsize=22)
        if xi != x2:
            q2 = plt.text(x2 - 200, -550, "$Q_2$", fontsize=22)
        else:
            q2 = plt.text(x2 + 300, -550, "$=Q_2$", fontsize=22)
        return p2, q2
    
    if i == "s":
        if ceiling:
            ps =plt.text(-400,y2, "$P_{C}$", fontsize=22)
        if floor:
            ps =plt.text(-400,y2, "$P_{F}$", fontsize=22)            
        qs = plt.text(x2 - 200, -500, "$Q_S$", fontsize=22)
        return ps, qs
    if i == "d":
        if ceiling:
            pd =plt.text(-400,y2, "$P_{C}$", fontsize=22)
        if floor:
            pd =plt.text(-400,y2, "$P_{F}$", fontsize=22)
        qd = plt.text(x2 - 200, -500, "$Q_D$", fontsize=22)
        return pd, qd
        
def setupAxes(frame):
    frame.axes.get_xaxis().set_visible(False)
    frame.axes.get_yaxis().set_visible(False)
    plt.ylim(ymin=0, ymax=10000)
    plt.xlim(xmin = 0, xmax = 10000)

    plt.xlabel("Quantity", fontsize=20)
    plt.ylabel("Price", fontsize = 20)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.tight_layout()
def findIntersection(curve1, curve2, inc):
    
    for x in range(len(curve1)):
        dist = curve1[x] - curve2[x]
        if abs(dist) < inc * 1.01:
            print(curve1[x])
            print(curve2[x])
            print("curve1 and curve2 are " + str(dist) + " units apart at x= " + str(x))
            
            return x, curve1[x]
def selectShiftCurve(demand, supply, shift1, shift2 = None, order=1):
    if order == 1:
        if shift1 == "Demand-Left":
            return np.arange(7000,-3000, -1 * inc)
        if shift1 == "Demand-Right":
            return np.arange(13000,3000, -1 * inc)
        if shift1 == "Supply-Left":
            return np.arange(1500, 11500, 1 * inc)
        if shift1 == "Supply-Right":
            return np.arange(-1500,8500, 1 * inc)
    if order == 2:
        if shift2 == "Demand-Left" and shift1 == "Demand-Left":
            return np.arange(5500,-4500, -1 * inc)
        if shift2 == "Demand-Left" and shift1 == "Demand-Right":
            return demand
        if shift2 == "Demand-Right" and shift1 == "Demand-Right":
            return np.arange(14500,4500, -1 * inc)
        if shift2 == "Demand-Right" and shift1 == "Demand-Left":
            return demand
        if shift2 == "Supply-Left" and shift1 == "Supply-Left":
            return np.arange(3000, 13000, 1 * inc)
        if shift2 == "Supply-Left" and shift1 == "Supply-Right":
            return supply
        if shift2 == "Supply-Right" and shift1 == "Supply-Right":
            return np.arange(-3000,7000, 1 * inc)
        if shift2 == "Supply-Right" and shift1 == "Supply-Left":
            return supply
        else:
            if shift2 == "Demand-Left":
                return np.arange(7000,-3000, -1 * inc)
            if shift2 == "Demand-Right":
                return np.arange(13000,3000, -1 * inc)
            if shift2 == "Supply-Left":
                return np.arange(1500, 11500, 1 * inc)
            if shift2 == "Supply-Right":
                return np.arange(-1500,8500, 1 * inc)
            

inc = 1                    
demandInc = inc
supplyInc = inc

Supply = np.arange(0,10000, 1 * supplyInc)
Demand = np.arange(10000,0, -1 * demandInc)
floor = False
ceiling = False
#ACL = np.arange(0, 5000, .5 * supplyInc)
#priceFloor = np.arange(1, 10000)
#priceFloor[priceFloor > 0] = 8000
#name = ""
pp = PdfPages('Money Graphs with Elastic Supply.pdf')


name = 'People Realize that Oats\nCan Be Used as Money'
Shift1 = "Demand-Right"
Shift2 = None#"Supply-Right"
supplyAndDemandWithShifts(Supply, Demand, Shift1, Shift2, ceiling=ceiling,floor=floor, inc= inc, name=name,pp= pp)

name = 'Farmers Develop Cost-Reducing\nTechnology for Oat Production'
#pp = PdfPages(name + '.pdf')
Shift1 = "Demand-Right"
Shift2 = "Supply-Right"
supplyAndDemandWithShifts(Supply, Demand, Shift1, Shift2, ceiling=ceiling,floor=floor, inc= inc, name=name,pp= pp)


name = 'Demand Increases'
Shift1 = "Demand-Right"
Shift2 = None#"Supply-Right"
supplyAndDemandWithShifts(Supply, Demand, Shift1, Shift2, ceiling=ceiling,floor=floor, inc= inc, name=name,pp= pp)

name = 'Demand Decreases'
#pp = PdfPages(name + '.pdf')
Shift1 = "Demand-Left"
Shift2 = None#"Supply-Right"
supplyAndDemandWithShifts(Supply, Demand, Shift1, Shift2, ceiling=ceiling,floor=floor, inc= inc, name=name,pp= pp)


name = 'Supply Increases'
#pp = PdfPages(name + '.pdf')
Shift1 = "Supply-Right"
Shift2 = None
supplyAndDemandWithShifts(Supply, Demand, Shift1, Shift2, ceiling=ceiling,floor=floor, inc= inc, name=name,pp= pp)

name = 'Supply Decreases'
#pp = PdfPages(name + '.pdf')
Shift1 = "Supply-Left"
Shift2 = None
supplyAndDemandWithShifts(Supply, Demand, Shift1, Shift2, ceiling=ceiling,floor=floor, inc= inc, name=name,pp= pp)



name = 'Minimum Price'
#pp = PdfPages(name + '.pdf')
Shift1 = None
Shift2 = None
floor = True
ceiling = False
supplyAndDemandWithShifts(Supply, Demand, Shift1, Shift2, ceiling=ceiling,floor=floor, inc= inc, name=name,pp= pp)



name = 'Maximum Price'
#pp = PdfPages(name + '.pdf')
Shift1 = None
Shift2 = None
floor = False
ceiling = True
supplyAndDemandWithShifts(Supply, Demand, Shift1, Shift2, ceiling=ceiling,floor=floor, inc= inc, name=name,pp= pp)


pp.close()
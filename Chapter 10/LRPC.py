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
def supplyAndDemandWithShifts(supply, demand, vertSupply=False, shift1=None, shift2=None, inc=1, name= "Loanable Funds", pp = PdfPages("Default.pdf")):
    pp = pp
    fig = plt.figure(dpi=128, figsize=(10,6))
    frame = plt.gca()                         
    plt.title(name, fontsize=20, ha='center')
    if vertSupply:
        supply = round(len(supply)/2)
    print(supply)
    if shift1:
#        plt.text(500, 5200, "$SRAS_0$",size=24)

        if (shift1 != "Supply-Left" and shift1 != "Supply-Right") or vertSupply == False:
            firstShift = selectShiftCurve(demand, supply, shift1,order=1)
        else:

            if shift1 == "Supply-Right":
                firstShift = 6750
            if shift1 == "Supply-Left":
                firstShift = 3250
    if shift2:
        secondShift = selectShiftCurve(demand, supply,shift1, shift2,order=2)
    i = 0
    
    if shift1 and shift2:
        xi,yi= findIntersection(supply, demand, inc)

        plotCurves(supply, demand,vertSupply, firstShift, secondShift, inc)
        placePrimaryText(vertSupply)
        p0, q0 = plotVertAndHorizLines(demand,supply,inc,i, "k--", vertSupply=vertSupply)
        i +=1

# Horizontal and Vertical Lines for First Shift        
        if shift1 == "Demand-Left" or shift1 == "Demand-Right":
            p1, q1 = plotVertAndHorizLines(firstShift, supply, inc,i, "k--",vertSupply=vertSupply, shift1=shift1,xi=xi,yi=yi)
            qt = plotVertAndHorizLines(firstShift, supply, inc,i, "k--",vertSupply=vertSupply, shift1=shift1,xi=xi,yi=yi,excess = True)

        if shift1 == "Supply-Left" or shift1 == "Supply-Right":
            p1, q1 = plotVertAndHorizLines(firstShift, demand, inc,i, "k--",vertSupply=vertSupply, shift1=shift1,xi=xi,yi=yi)
            qt = plotVertAndHorizLines(firstShift, demand, inc,i, "k--",vertSupply=vertSupply, shift1=shift1,xi=xi,yi=yi,excess = True)

        i += 1
        if (shift2 == "Demand-Left" or shift2 == "Demand-Right"):
            if (shift1 == "Demand-Left" or shift1 == "Demand-Right"):
                p2, q2 = plotVertAndHorizLines(secondShift, supply, inc,i, "k--", xi, yi,vertSupply=vertSupply, shift2=shift2)
                if shift1 != shift2:
                    p0.remove
                    q0.remove                    
            if (shift1 == "Supply-Left" or shift1 == "Supply-Right"):
                x1, y1 = findIntersection(demand, firstShift, inc)
                p2, q2 = plotVertAndHorizLines(secondShift, firstShift, inc, i, "k--", x1, yi,vertSupply=vertSupply,shift2=shift2)
                if (shift2 == "Demand-Left" and shift1 == "Supply-Right") or (shift2 == "Demand-Right" and shift1 == "Supply-Left") :
                    q0.remove
        if shift2 == "Supply-Left" or shift2 == "Supply-Right":
            if (shift1 == "Demand-Left" or shift1 == "Demand-Right"):
                p2, q2 = plotVertAndHorizLines(secondShift, firstShift, inc,i, "k--", xi, yi,vertSupply=vertSupply,shift2=shift2)
                if (shift1 == "Demand-Left" and shift2 == "Supply-Right") or (shift1 == "Demand-Right" and shift2 == "Supply-Left") :
                    q0.remove
            if (shift1 == "Supply-Left" or shift1 == "Supply-Right"):
                p2, q2 = plotVertAndHorizLines(secondShift, demand, inc,i, "k--", xi, yi,vertSupply=vertSupply,shift2=shift2)
                if shift1 != shift2:
                    p0.remove
                    q0.remove                                    
    if shift1 == None and shift2 == None:
        plotCurves(supply, demand, vertSupply = vertSupply)
        p0, q0 = plotVertAndHorizLines(demand,supply,inc,i, "k--",vertSupply=vertSupply)


    if shift1 and not shift2:
        placePrimaryText(vertSupply)
        p0, q0 = plotVertAndHorizLines(demand,supply,inc,i, "k--",vertSupply=vertSupply)

        # Horizontal and Vertical Lines for First Shift        
        i +=1
        if shift1 == "Demand-Left" or shift1 == "Demand-Right":
            p1, q1 = plotVertAndHorizLines(firstShift, supply, inc,i, "k--",vertSupply=vertSupply, shift1=shift1)
            qt = plotVertAndHorizLines(firstShift, supply, inc,i, "k--",vertSupply=vertSupply, shift1=shift1,excess = True)

        if shift1 == "Supply-Left" or shift1 == "Supply-Right":
            p1, q1 = plotVertAndHorizLines(firstShift, demand, inc,i, "k--",vertSupply=vertSupply, shift1 = shift1)
            qt = plotVertAndHorizLines(firstShift, demand, inc,i, "k--",vertSupply=vertSupply, shift1=shift1,excess = True)

        plotCurves(supply, demand, vertSupply,firstShift, None, inc)


    if not shift1 and shift2:
        plotCurves(supply, demand,vertSupply, None, secondShift, inc)
        p0, q0 = plotVertAndHorizLines(demand,supply,inc,i, "k--",vertSupply=vertSupply)

        # Horizontal and Vertical Lines for First Shift        
        i +=1
        if shift1 == "Demand-Left" or shift1 == "Demand-Right":
            p1, q1 = plotVertAndHorizLines(firstShift, supply, inc,i, "k--",vertSupply=vertSupply,xi=xi,yi=yi)
        if shift1 == "Supply-Left" or shift1 == "Supply-Right":
            p1, q1 = plotVertAndHorizLines(firstShift, demand, inc,i, "k--",vertSupply=vertSupply,xi=xi,yi=yi)

  
    
    placePrimaryText(vertSupply)
    placeShiftText(shift1, shift2,vertSupply=vertSupply)
    setupAxes(frame)
    plt.savefig(name.replace("\n"," "))

    pp.savefig(fig)
#    plt.close()
#    pp.close()

def placePrimaryText(vertSupply=False):
    #plt.text(x,y,text,fontsize)
    p = plt.text(-600, 10000, "$\pi_e$", fontsize=24)
    if vertSupply == False:
        s = plt.text(8200, 8800,"$SRAS_0$", fontsize = 22)
    else:
        s = plt.text(5100, 8800, "$LRPC_0$", fontsize = 22)
    d = plt.text(7100, 3000,"$SRPC_1$", fontsize = 22)
    q = plt.text(10000, -650, "$U$", fontsize=24)
    return p , s , d , q 
    
def placeShiftText(shift1, shift2=None, vertSupply=False):    
    if shift1 == None:
        if (shift2):
            placeShiftText(shift2)
        else:            
            return
    
    if shift1 == "Demand-Left":
        plt.text(6000, 1100,"$SRPC_0$", fontsize = 22)
    if shift1 == "Demand-Right":
        plt.text(7100, 5000,"$SRPC_0$", fontsize = 22)
    if shift1 == "Supply-Left":
        if vertSupply == False:
            plt.text(6600, 8800,"$LRPC_1$", fontsize = 22)
        else:
            plt.text(3350, 8800,"$LRPC_1$", fontsize = 22)
    if shift1 == "Supply-Right":
        if vertSupply == False:        
            plt.text(8500, 7600,"$LRPC_1$", fontsize = 22)
        else:
            plt.text(6850, 8800,"$LRPC_1$", fontsize = 22)

# safety check . . . 
    if shift1 and shift2:
        if shift2 == "Demand-Left":
            if shift1 == "Supply-Left" or shift1 == "Supply-Right":
                plt.text(6200, 1000,"$SRPC_0$", fontsize = 22)
            if shift1 == "Demand-Left":    
                plt.text(4000, 1600,"$SRPC_2$", fontsize = 22)
            if shift1 == "Demand-Right":
                plt.text(8200, 2000,"$SRPC_{0,2}$", fontsize = 22) # same as initial
        if shift2 == "Demand-Right":
            if shift1 == "Supply-Left" or shift1 == "Supply-Right":
                plt.text(9000, 3850,"$SRPC_0$", fontsize = 22)
            if shift1 == "Demand-Left":
                plt.text(8200, 2000,"$SRPC_{0,2}$", fontsize = 22) # same as initial
            if shift1 == "Demand-Right":
                plt.text(9000, 5750,"$U_{D_2}$", fontsize = 22)
                

        if shift2 == "Supply-Left":
            if shift1 == "Demand-Left" or shift1 == "Demand-Right":
                plt.text(6600, 8800,"$U_{S_1$", fontsize = 22)                
            if shift1 == "Supply-Left":
                plt.text(5100, 8800,"$U_{S_2$", fontsize = 22)
            if shift1 == "Supply-Right":
                plt.text(7755, 8800,"$U_{S_2$", fontsize = 22) # same as initial

        if shift2 == "Supply-Right":
            if shift1 == "Demand-Left" or shift1 == "Demand-Right":
                plt.text(8500, 7600,"$U_{S_1$", fontsize = 22)                
            if shift1 == "Supply-Left":
                plt.text(7755, 8800,"$U_{S_{0,2}$", fontsize = 22) # same as initial
            if shift1 == "Supply-Right":
                plt.text(9750, 6000,"$U_{S_2$", fontsize = 22)        
        
    


def plotCurves(supply, demand, vertSupply=False, shift1=None, shift2=None,  inc=1):
    # plt.plot((x1,x2), (y1,y2), linestyle/color, linewidth)
    if vertSupply == False:
        plt.plot(supply, 'C0-', linewidth=3)
    else:
        plt.axvline(x=supply, color = 'C0', linewidth=3)
    plt.plot(demand, 'C3-', linewidth=3)    
    try:
        if isinstance(shift1,np.ndarray):
            plt.plot(shift1, 'C0-', linewidth=3)
        else:
            if isinstance(shift1, int):
                plt.axvline(x=shift1, color = 'C3', linewidth=3)
    except NameError:
        print("shift1 = None")    
#    if not np.all([shift2, supply]) and not np.all([shift2, demand]):
    try:
        if isinstance(shift2,np.ndarray):
            plt.plot(shift2, 'C3-', linewidth=3)
        else:
            if isinstance(shift2, int):
                plt.axvline(x=shift2)
    except NameError:
        print("shift1 = None")    

def plotVertAndHorizLines(curve1, curve2, inc, i, line, 
                          xi = None, yi = None, vertSupply=False,shift1=None, shift2=None, excess=False):
    

    if excess:
#        SRAS = np.array([5000]*10000)
        SRAS = 5000
        pt, qt = findIntersection(SRAS,curve1,1)
        plt.plot((0,qt), (pt,pt), line, linewidth= 1.5)
        plt.plot((qt, qt), (0, pt), line, linewidth=1.5)
#        pt =plt.text(-600,y2, "$\pi_{e_1$", fontsize=20)
        if not isinstance(curve1, int):
            qt = plt.text(qt - 200, -650, "$U_t$", fontsize=20)
        else:
#            qt = plt.text(qt - 200, -650, "$U_{0,t}$", fontsize=20)
            print("M Shift")
        return qt
    
    x2,y2 = findIntersection(curve1, curve2, inc)
    
#    plt.plot((x2, x2), (0, y2), line, linewidth=1.5)
    plt.plot((0,x2), (y2, y2), line,linewidth=1.5)
    if i == 0:    
        p0 =plt.text(-700,y2, "$\pi_{e_1}$", fontsize=20)
        q0 = plt.text(x2 - 200, -650, "$U_{N_0}$", fontsize=20)
        return p0, q0

    if i == 1:
        p1 = plt.text(-700,y2, "$\pi_{e_0}$", fontsize=20)
        if vertSupply:
            if shift1=="Supply-Left" or shift1 == "Supply-Right":
                q1 = plt.text(x2 - 200, -650, "$U_{N_1}$", fontsize=20)
            else:
                q1 = plt.text(x2 - 200, -650, "", fontsize=20)
                
        else:
            if shift1=="Supply-Left" or shift1 == "Supply-Right":
                q1 = plt.text(x2 - 200 , -650, "$U_{N_1}$", fontsize=20)
            
        return p1, q1
    if i == 2:
        if yi != y2 and abs(yi - y2) > 200:
            print("yi - y2", yi - y2)
            p2 = plt.text(-700,y2, "$\pi_{e_2}$", fontsize=20)
        else:
            p2 = plt.text(-700,y2, "$\pi_{e_{0,2}}$", fontsize=20)
        if xi != x2:
            q2 = plt.text(x2 - 200, -650, "$U_2$", fontsize=20)
        else:
            q2 = plt.text(x2 + 200, -650, "$_{,2}$", fontsize=20)
            
        return p2, q2

def setupAxes(frame):
    frame.axes.get_xaxis().set_visible(False)
    frame.axes.get_yaxis().set_visible(False)
    plt.ylim(0, 10000)
    plt.xlim(xmin = 0, xmax = 10000)

    plt.xlabel("Real Income", fontsize=20)
    plt.ylabel("Price Level", fontsize = 20)
    plt.tick_params(axis='both', which='major', labelsize=16)

def findIntersection(curve1, curve2, inc):
    print(curve1, curve2)
    if isinstance(curve1, int) and isinstance(curve2, int):
        print("WHA?")
        return curve1, curve2
    else:
        try:
            for x in range(len(curve1)):
                dist = curve1[x] - curve2[x]
                if abs(dist) < inc * 1.01:
                    print(curve1[x])
                    print(curve2[x])
                    print("curve1 and curve2 are " + str(dist) + " units apart at x= " + str(x))
                    
            return x, curve1[x]
        except:
            try:
                return curve1, curve2[curve1]
            except:
                return curve2, curve1[curve2]
#                print("Oh well...")
  
def createADShift(shift, root):
    if shift != None: 
        if "Supply" not in shift:
            if "Left" in shift:
                posNeg = -1
            else:
                posNeg = 1
            
            newRoot = root + 800 * posNeg
            ADV1 = (newRoot) ** 2 

            demandShift = np.arange(10000)
            #SRAS = np.arange(6000)
            for i in range(len(Demand)):
                if i != 0:
                    demandShift[i] = ADV1 / i
            return demandShift, newRoot
def selectShiftCurve(demand, supply, shift1, shift2 = None, order=1):
    print(shift1)
    if order == 1:
        if shift1 == "Demand-Left":
            return np.arange(7000,-3000, -1 * inc)
        if shift1 == "Demand-Right":
            return np.arange(12000,2000, -1 * inc)
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
                return np.arange(8000,-2000, -1 * inc)
            if shift2 == "Demand-Right":
                return np.arange(11450,1450, -1 * inc)
            if shift2 == "Supply-Left":
                return np.arange(1500, 11500, 1 * inc)
            if shift2 == "Supply-Right":
                return np.arange(-1500,8500, 1 * inc)

inc = 1                    
demandInc = inc
supplyInc = inc

Supply = np.arange(0,10000, 1 * supplyInc)
Demand = np.arange(10000,0, -1 * demandInc)
#ADV1 = 5000 ** 2
#Demand  = np.arange(10000)
#SRAS = np.arange(6000)
#for i in range(len(Demand)):
#    if i != 0:
#        Demand[i] = ADV1 / i

vertSupply = True
#ACL = np.arange(0, 5000, .5 * supplyInc)
#priceFloor = np.arange(1, 10000)
#priceFloor[priceFloor > 0] = 8000
#name = ""
pp = PdfPages('Money Supply and Demand Graphs with Inelastic Supply.pdf')

name = 'Expectations Augmented Phillips Curve'
#pp = PdfPages(name + '.pdf')
Shift1 = None#"Demand-Right"
Shift2 = None#"Supply-Right"
supplyAndDemandWithShifts(Supply, Demand, vertSupply,Shift1, Shift2, inc, name, pp)

name = 'Disinflation and Short-run Increase in Unemployment'

#pp = PdfPages(name + '.pdf')
Shift1 = "Demand-Right"
Shift2 = None#"Supply-Right"
supplyAndDemandWithShifts(Supply, Demand, vertSupply,Shift1, Shift2, inc, name, pp)

name = 'Inflation and Short-run Fall in Unemployment'

Shift1 = "Demand-Left"
Shift2 = None#"Supply-Right"
supplyAndDemandWithShifts(Supply, Demand, vertSupply,Shift1, Shift2, inc, name, pp)

name = 'Increase in Natural Rate of Unemployment'
Shift1 = "Supply-Right"
Shift2 = None#"Supply-Right"
supplyAndDemandWithShifts(Supply, Demand, vertSupply,Shift1, Shift2, inc, name, pp)

name = 'Decrease in Natural Rate of Unemployment'
Shift1 = "Supply-Left"
Shift2 = None#"Supply-Right"
supplyAndDemandWithShifts(Supply, Demand, vertSupply,Shift1, Shift2, inc, name, pp)

#name = 'Money Production Responds\nto Increase in Real Income'
#Shift1 = "Supply-Right"
#Shift2 = "Demand-Right"
#supplyAndDemandWithShifts(Supply, Demand, vertSupply,Shift1, Shift2, inc, name, pp)


#
#name = 'Demand Shifts Left'
#pp = PdfPages(name + '.pdf')
#Shift1 = "Demand-Left"
#Shift2 = ""
#supplyAndDemandWithShifts(Supply, Demand, Shift1, Shift2, inc, name, pp)
##pp.close()
#
#name = 'Supply Shifts Right'
#pp = PdfPages(name + '.pdf')
#Shift1 = "Supply-Right"
#Shift2 = ""
#supplyAndDemandWithShifts(Supply, Demand, Shift1, Shift2, inc, name, pp)
##pp.close()
#
#name = 'Supply Shifts Left'
#pp = PdfPages(name + '.pdf')
#Shift1 = "Supply-Left"
#Shift2 = ""
#supplyAndDemandWithShifts(Supply, Demand, Shift1, Shift2, inc, name, pp)
##pp.close()
#
#name = 'Demand and Supply Shift Right'
#pp = PdfPages(name + '.pdf')
#Shift1 = "Demand-Right"
#Shift2 = "Supply-Right"
#supplyAndDemandWithShifts(Supply, Demand, Shift1, Shift2, inc, name, pp)
pp.close()
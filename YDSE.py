import math 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.widgets import Slider, Button



#Double slit experiment - Interference and Diffraction

# some theory


# ld = h/mv  => de broglie
# sin(x)= (m.ld)/d where d is the distance between the slits.
# I= I0 (sin(B)/B)**2  
# B= pi.a.sin(x)/ld where a is the width of the fringe
# Y axis is I/I0
# X axis is d

X = np.arange(-0.005,0.005,0.00001)
b = 100*(10**-6)
w = 500*(10**-9)
d = 50*(10**-2)
a= 1*10**-3


ak=10**-4                    #slider
b1=10**-3                    #slider
h=6.62*(10**-34)
m= 9.1*(10**-31)
v=3*(10**7)                 #just an arbitrary value for now
theta = -0.005
i0=100.00                  #arbitrary value
S= 0.01

ld = h/m*v
T=[]
I=[]
X = np.arange(-0.005,0.005,0.00001)


while theta< 0.005:
    T.append(theta)
    b1=(math.pi * ak * math.sin(theta))
    i=i0 * (math.sin(b1)/b1)**2
    I.append(i/i0)
    theta=theta+0.00001
Its = np.array(I)
Th = np.array(T)
 
 
plt.title("Double Slit Experiment")
plt.xlabel("X axis" )
plt.ylabel("Y axis" )
plt.plot(Th,Its, color="black")





Y = (((np.sin((np.pi*b*X)/(w*d)))/((np.pi*b*X)/(w*d)))**2)*((np.cos((np.pi*a*X)/(w*d)))**2)

Y1 = (((np.sin((np.pi*b*X)/(w*d)))/((np.pi*b*X)/(w*d)))**2)

Y2 = ((np.cos((np.pi*a*X)/(w*d)))**2)

 
 
plot = plt.plot(X,Y1,color = "red")
plot = plt.plot(X,Y,color = "green")
#plot = plt.plot(X,Y2,color = "gray")
plt.xlabel("Distance from center")
plt.ylabel("Intensity")

plt.show()
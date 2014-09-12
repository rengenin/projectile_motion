#!/usr/bin/python
from math import sin, cos, sqrt, pi, radians, degrees
import numpy as np
import matplotlib.pyplot as plt

'''
Projectile motion with linear air resistance

Plots flight path of projectile as well as kinetic and 
potential energies versus time during flight.

Written using functions.
'''

m = float(10) #mass of projectile in grams
r = float(0.01) #radius of projectile in meters
C = float(0.47) #drag coefficient (unitless)
theta = radians(float(45.0)) #launch angle of projectile in degrees
v = float(30.0) #initial velocity in meters per sec
den = 1225.0 #g/m^3 density of air at sea level
g = 9.8 #gravitational acceleration in meters per sec
delt = 0.01 #s time resolution

#position array
x=[]
y=[]
#velocity arrays
vx=[]
vy=[]
#acceleration arryas
ax=[]
ay=[]

def cross_section(r):
    A = pi*r**2 #cross section of projectile
    return A

def drag_force(den,A,C):
    D = (den*A*C)/2.0 #drag force
    return D
 
def intial_position(x,y):
    #initial position
    x.insert(1,0.0) #m
    y.insert(1,1.0) #m
    return x, y

def intial_velocity(v,vx,vy):
    #initial velocity components
    vx.insert(1,v*cos(theta))
    vy.insert(1,v*sin(theta))
    return vx, vy

def intial_acceleration(D,m,v,vx,vy):
    #initial acceleration components
    ax.insert(1, -(D/m)*v*vx[0])
    ay.insert(1, -g-(D/m)*v*vy[0])
    return ax, ay

def kinematics(D,x,y,v,vx,vy,ax,ay):
    i=2
    while(y[i-2] >= 0.0):
        vx.insert(i, vx[i-2] + ax[i-2]*delt)
        vy.insert(i, vy[i-2] + ay[i-2]*delt)
        x.insert(i, x[i-2] + vx[i-2]*delt + (ax[i-2]*delt**2)/2)
        y.insert(i, y[i-2] + vy[i-2]*delt + (ay[i-2]*delt**2)/2)
        ax.insert(i, -(D/m)*v*vx[i-1])
        ay.insert(i, -g-(D/m)*v*vy[i-1])
        i=i+1
    x.pop(i-2)
    y.pop(i-2)
    vx.pop(i-2)
    vy.pop(i-2)
    ax.pop(i-2)
    ay.pop(i-2)
    return x,y,vx,vy,ax,ay

def final_velocity(vx,vy):
    vf = sqrt(vx[-1]**2 + vy[-1]**2) #final velocity in meters per second
    vf = round(vf, 3)
    print 'Final Velocity:', vf, 'Meters per Second'
    return vf

def kinetic_energy(m,vx,vy):
    ke = [0]*len(vx)
    for n in range(0, len(ke)):
        ke[n] = 0.001*0.5*m*sqrt(vx[n]**2 + vy[n]**2)
    return ke

def final_kinetic_energy(m,vf):    
    keF = 0.001*0.5*m*vf**2 #kinetic engergy in Joules
    keF = round(keF, 3)
    print 'Kinetic Energy:', keF, 'Joules'
    return keF 

def potential_energy(m,g,y):
    U = [0.001*m*g*n for n in y] #potential energy in Joules (kg*m**2/s)
    return U

def flight_time(delt,x):
    step = []
    n = 0
    for n in range(0, len(x)):
        n =  n + 1
        step.append(n)       
    T = [m*delt for m in step] #time of flight = time resolution * itterations
    return T

def plots(x,y,T,ke,U):
    Pos = plt.subplot(3,1,1)
    Kin = plt.subplot(3,1,2)
    Pot = plt.subplot(3,1,3)
    plt.subplots_adjust(hspace=0.7)
    #position
    Pos.plot(x,y,'g^')
    Pos.set_xlabel('Meters')
    Pos.set_ylabel('Meters')
    Pos.set_title('2D Flight Path')
    #kinetic energy versus time 
    Kin.plot(T,ke)
    Kin.set_xlabel('milliseconds')
    Kin.set_ylabel('Joules')
    Kin.set_title('Kinetic Energy versus Time')
    #potential energy versus time
    Pot.plot(T,U,'r--')
    Pot.set_xlabel('milliseconds')
    Pot.set_ylabel('Joules')
    Pot.set_title('Potential Engery versus Time')
    plt.show()

def main(x,y,vx,vy):
    A = cross_section(r)
    D = drag_force(den,A,C)
    x, y = intial_position(x,y)
    vx, vy = intial_velocity(v,vx,vy)
    ax, ay = intial_acceleration(D,m,v,vx,vy)
    x, y, vx, vy, ax, ay = kinematics(D,x,y,v,vx,vy,ax,ay)
    vf = final_velocity(vx,vy)
    ke = kinetic_energy(m,vx,vy)
    keF = final_kinetic_energy(m,vf)
    U = potential_energy(m,g,y)
    T = flight_time(delt,x)
    plots(x,y,T,ke,U)

main(x,y,vx,vy)

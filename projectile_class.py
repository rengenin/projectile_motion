#!/usr/bin/python
from __future__ import division
from math import sin, cos, sqrt, pi, radians, degrees
import matplotlib.pyplot as plt

'''
Projectile motion with linear air resistance.

Plots flight path of projectile as well as kinetic and 
potential energies versus time during flight.

Written using classes.
'''

#Initial Conditions
theta = radians(float(45.0)) #launch angle of projectile in degrees
v = float(30) #initial velocity in meters per sec
den = 1225.0 #g/m^3 density of air at sea level
g = 9.8 #gravitational acceleration in meters per sec
delt = 0.01 #s time resolution

#position array
x=[]
y=[]
#velocity arrays
vx=[]
vy=[]
#acceleration arrays
ax=[]
ay=[]

class projectile:

	def __init__(self,r,m,C):
	    self.r = r #Radius of projectile cross section in Meters
	    self.C = C #Coefficient of drag
            self.m = m #Mass in grams

	def cross_section(self):
	    return pi*self.r**2 #Cross section area (assuming circular profile)

	def drag_force(self):
      	    return 0.5*den*projectile.cross_section(self)*self.C

class projectile_motion:

    def __init__(self,x,y,v,vx,vy,ax,ay,D,m):
        self.x = x #X position in meters
        self.y = y #Y position in meters
        self.v = v #Initial velocity in m/s
        self.vx = vx #X velocity in m/s
        self.vy = vy #Y velocity in m/s
        self.ax = ax #X acceleration in m/s^2
        self.ay = ay #Y acceleration in m/s^2
        self.D = D #Drag force calculated in Sphere
        self.m = m #Mass of object in grams

    def initial_position(self):
        return self.x.insert(1,0.0), self.y.insert(1,1.0)

    def initial_velocity(self):
        return self.vx.insert(1,self.v*cos(theta)), self.vy.insert(1,self.v*sin(theta))

    def initial_acceleration(self):
        return self.ax.insert(1, -(self.D/self.m)*self.v*self.vx[0]), self.ay.insert(1, -g-(self.D/self.m)*self.v*self.vy[0])
    #Iterate through equations of motion
    def kinematics(self):
        i=2
        while(self.y[i-2] >= 0.0):
                self.vx.insert(i, self.vx[i-2] + self.ax[i-2]*delt)
                self.vy.insert(i, self.vy[i-2] + self.ay[i-2]*delt)
                self.x.insert(i, self.x[i-2] + self.vx[i-2]*delt + (self.ax[i-2]*delt**2)/2)
                self.y.insert(i, self.y[i-2] + self.vy[i-2]*delt + (self.ay[i-2]*delt**2)/2)
                self.ax.insert(i, -(self.D/self.m)*self.v*self.vx[i-1])
                self.ay.insert(i, -g-(self.D/self.m)*self.v*self.vy[i-1])
                i=i+1
        self.x.pop(i-2)
        self.y.pop(i-2)
        self.vx.pop(i-2)
        self.vy.pop(i-2)
        self.ax.pop(i-2)
        self.ay.pop(i-2)
        return self.x,self.y,self.vx,self.vy,self.ax,self.ay

    def final_velocity(self):
        self.vf = round(sqrt(self.vx[-1]**2 + self.vy[-1]**2), 3) #final velocity in meters per second
        print 'Final Velocity:', self.vf, 'Meters per Second'
        return self.vf

    def kinetic_energy(self):
        self.ke = [0]*len(self.vx)
        for n in range(0, len(self.ke)):
            self.ke[n] = 0.001*0.5*self.m*sqrt(self.vx[n]**2 + self.vy[n]**2)
        return self.ke

    def final_kinetic_energy(self):
        self.keF = round(0.001*0.5*self.m*self.vf**2, 3) #kinetic engergy in Newtons
        print 'Kinetic Energy:', self.keF, 'Joules'
        return self.keF 

    def potential_energy(self):
        self.U = [0.001*self.m*g*n for n in y] #potential energy in Joules (g*m**2/s)
        return self.U

    def flight_time(self):
        self.step = []
        i = 0
        for i in range(0, len(self.x)):
            i =  i + 1
            self.step.append(i)       
        self.T = [j*delt for j in self.step] #time of flight = time resolution * itterations
        return self.T

def plots(x,y,T,ke,U):
    Pos = plt.subplot(3,1,1) #Position
    Kin = plt.subplot(3,1,2) #Kinetic Energy
    Pot = plt.subplot(3,1,3) #Potential Energy
    plt.subplots_adjust(hspace=0.7)
    #Position
    Pos.plot(x,y,'g^')
    Pos.set_xlabel('Meters')
    Pos.set_ylabel('Meters')
    Pos.set_title('2D Flight Path')
    #Kinetic Energy versus Time 
    Kin.plot(T,ke)
    Kin.set_xlabel('milliseconds')
    Kin.set_ylabel('Joules')
    Kin.set_title('Kinetic Energy versus Time')
    #Potential Energy versus Time
    Pot.plot(T,U,'r--')
    Pot.set_xlabel('milliseconds')
    Pot.set_ylabel('Joules')
    Pot.set_title('Potential Engery versus Time')
    plt.show()

def main(x,y,vx,vy):
	ball = projectile(0.01,10,0.47) #Radius, Mass, Drag Coefficient
	A = ball.cross_section()
	C = ball.C
	m = ball.m
	D = ball.drag_force()
	motion = projectile_motion(x,y,v,vx,vy,ax,ay,D,m)
	pos = motion.initial_position()
	vel = motion.initial_velocity()
  	acc = motion.initial_acceleration()
  	flight = motion.kinematics()
  	vf = motion.final_velocity()
  	ke = motion.kinetic_energy()
  	kef = motion.final_kinetic_energy()
  	U = motion.potential_energy()
  	T = motion.flight_time()
	plots(x,y,T,ke,U)

main(x,y,vx,vy)

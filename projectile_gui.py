from math import sin, cos, sqrt, pi, radians, degrees
import numpy as np
import matplotlib.pyplot as plt
from Tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg


def projectile():
	try:
		theta = float(entryAng.get())
		m = float(entryMass.get())
		v = float(entryVel.get())
		r = float(entryRad.get())
		C = float(entryDrag.get())

		g = 9.8 #gravitational acceleration in meters per sec
		vx = v*cos(radians(theta)) # x component of initial velocity
		vy = v*sin(radians(theta)) # y component of initial velocity

		den = 1225.0 #g/m^3 density of air at sea level
		den2 = 909.3 #g/m^3 density of air at 3000 meters
		A = 4*pi*r**2 #surface area of projectile
		D = (den*A*C)/2.0 #drag force

		#acceleration components w/ drag

		#delt is the time interval per iteration
		delt = 0.01 #s

		#initial position
		x = 0 #m
		y = 1 #m

		ylist=[]
		xlist=[]
		vylist=[]
		vxlist=[]

		#loop through each equation of motion
		while(y >= 0.0):
			if m == 0:
				m = 0.00001
				continue
	  		ax = -(D/m)*v*vx
	  		ay = -g-(D/m)*v*vy
	  		vx = vx + ax*delt
	  		vy = vy + ay*delt  
	  		x = x + vx*delt + (ax*delt**2)/2
	  		y = y + vy*delt + (ay*delt**2)/2
			ylist.append(y)
			xlist.append(x)
			vylist.append(vy)
			vxlist.append(vx)      

		vy_len = len(vylist) - 1
		vx_len = len(vxlist) - 1

		vf = sqrt(vxlist[vx_len]**2 + vylist[vy_len]**2) #final velocity
		vf = round(vf, 3)
		ke = .5*m*vf**2 #kinetic energy (gm^2)/s^2
		ke = ke*.001 #kinetic engergy in Newtons
		ke = round(ke, 3) 

		#Result display
		Vfin.config(text=vf) #Final velocity
		Ken.config(text=ke) #Kinetic energy

		#plots
		plt.plot(xlist,ylist,marker='o')
		plt.ylabel('Altitude in Meters')
		plt.xlabel('Range in Meters')
		plt.title('Projectile Position with Time')
		plt.gcf().canvas.draw()
		#plt.clf()
		
	except ValueError:
		Vfin.config(text='Numbers Dummy')
		Ken.config(text='Numbers Dummy')

def clear():
	plt.clf()
	plt.gcf().canvas.draw()


# create the application window and add a Frame
window = Tk()
window.title("Projectile Motion with drag")
inPut = Frame()
inPut.grid(padx=5, pady=5) # pad top and left of frame 5 pixels before grid

# GUI labels
labelAng = Label(inPut, text="Projectile angle:")
labelAng.grid(row=1, column=1, sticky=S+E)
labelDeg = Label(inPut, text="Degrees")
labelDeg.grid(row=1, column=3, sticky=S+W)

labelMass = Label(inPut, text="Projectile mass:")
labelMass.grid(row=2, column=1, sticky=S+E)
labelGram = Label(inPut, text="Grams")
labelGram.grid(row=2, column=3, stick=S+W)

labelVel = Label(inPut, text="Initial velocity:")
labelVel.grid(row=3, column=1, sticky=S+E)
labelMs = Label(inPut, text="Meters Per Second")
labelMs.grid(row=3, column=3, stick=S+W)

labelRad = Label(inPut, text="Projectile Radius:")
labelRad.grid(row=4, column=1, sticky=S+E)
labelSize = Label(inPut, text="Meters")
labelSize.grid(row=4, column=3, stick=S+W)

labelDrag = Label(inPut, text="Drag Coefficient:")
labelDrag.grid(row=5, column=1, sticky=S+E)

labelVfin = Label(inPut, text="Final Velocity:")
labelVfin.grid(row=6, column=1, sticky=S+E)
labelSpeed = Label(inPut, text="Meters Per Second")
labelSpeed.grid(row=6, column=3, sticky=S+W)

labelKen = Label(inPut, text="Kinetic Energy:")
labelKen.grid(row=7, column=1, sticky=S+E)
labelEng = Label(inPut, text="Newtons")
labelEng.grid(row=7, column=3, sticky=S+W)

# create and add space for user entry of text
entryAng = Entry(inPut, width=7)
entryAng.grid(row=1, column=2)
entryAng.insert(0, 45)

entryMass = Entry(inPut, width=7)
entryMass.grid(row=2, column=2)
entryMass.insert(0, 1)

entryVel = Entry(inPut, width=7)
entryVel.grid(row=3, column=2)
entryVel.insert(0, 350)

entryRad = Entry(inPut, width=7)
entryRad.grid(row=4, column=2)
entryRad.insert(0, 0.01)

entryDrag = Entry(inPut, width=7)
entryDrag.grid(row=5, column=2)
entryDrag.insert(0, 0)


# Displaying results
Vfin = Label(inPut)
Vfin.grid(row=6, column=2)
Ken = Label(inPut)
Ken.grid(row=7, column=2)


btnCalc = Button(inPut, text="Calculate", command=projectile)
btnCalc.grid(row=8, column=1)
btnClear = Button(inPut, text="Clear Plot", command=clear)
btnClear.grid(row=8, column=3)

fig = plt.figure()

canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().delete("all")
canvas.get_tk_widget().grid(row=0,column=1)

mainloop() # start the application

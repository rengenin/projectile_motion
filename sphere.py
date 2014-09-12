#!/usr/bin/python

'''Playing with classes'''
#Let's define a sphere
from __future__ import division
from math import pi

class Sphere:
	def __init__(self,r):
		self.r = r
	description = "Imagine a ball..."
	def diameter(self):
		return 2*self.r
	def circumference(self):
		return 2*pi*self.r
	def surfArea(self):
	    return 4*pi*self.r**2 #surface area of a sphere
	def volume(self):
		return (4/3)*pi*self.r**3 #volume of sphere

ball = Sphere(3)
ball.description("Imagine a ball...")

print "Diameter", ball.diameter()
print "Circumference", ball.circumference()
print "Surface Area", ball.surfArea()
print "Volume", ball.volume()

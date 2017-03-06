import	random
import	math
import 	numpy as np
import 	time
import 	matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

X_SIZE			= 1000
Y_SIZE			= 1000
Z_SIZE			= 1000
MAX_VEL			= 50
MIN_DISTANCE	= 50
BOID_NUMBER		= 300


class Boid(object):
	pos = [0.0,0.0,0.0]
	vel = [0.0,0.0,0.0]
	def __init__(self):
		self.pos	= [float(random.randint(0,X_SIZE)),float(random.randint(0,Y_SIZE)),float(random.randint(0,Z_SIZE))]
		self.vel 	= [float(random.randint(0,MAX_VEL)),float(random.randint(0,MAX_VEL)),float(random.randint(0,MAX_VEL))]

	def updatePos(self):
		for x in range(len(self.pos)):
			self.pos[x] += self.vel[x]

		for x in range(len(self.pos)):
			if self.pos[x] < 0:
				self.pos[x] = 50
			if self.pos[x] > 1000:
				self.pos[x] = 950
 
	def updateVel(self,boids):
		v1 = self.matchVel(boids)
		v2 = self.avoid(boids)
		v3 = self.matchPos(boids)

		for x in range(len(self.vel)):
			self.vel[x] += v1[x]
			self.vel[x] += v2[x]
			self.vel[x] += v3[x]


		speed = self.calcSpeed()
		if speed > MAX_VEL:
			self.vel=[(x*MAX_VEL)/speed for x in self.vel]


	def boidDistance(self,other):
		s = 0.0
		for x in range(len(self.pos)):
			s += (self.pos[x]-other.pos[x])**2
		return math.sqrt(s)

	def calcSpeed(self):
		s = 0.0
		for x in range(len(self.vel)):
			s += (self.vel[x])**2
		return math.sqrt(s)

	def matchVel(self,boids):
		vel = [0.0,0.0,0.0]
		for x in boids:
			if x is not self:
				vel[0]	+= x.vel[0]
				vel[1]	+= x.vel[1]
				vel[2]	+= x.vel[2]
		return [((vel[x]/(len(boids)-1))-self.vel[x])/2 for x in range(len(vel))]

	def avoid(self,boids):
		vel = [0.0,0.0,0.0]
		for x in boids:
			if x is not self:
				if self.boidDistance(x)<MIN_DISTANCE:
					vel[0] -= self.pos[0]-x.pos[0]
					vel[1] -= self.pos[1]-x.pos[1]
					vel[2] -= self.pos[2]-x.pos[2]
		return vel

	def matchPos(self,boids):
		pos=[0.0,0.0,0.0]
		for x in boids:
			if x is not self:
				for y in range(len(x.pos)):
					pos[y] += x.pos[y]
		return  [((pos[x]/(len(boids)-1))-self.pos[x]) for x in range(len(pos))]

if __name__ == '__main__':
	boids = []
	for boid in range(BOID_NUMBER):
		b=Boid()
		boids.append(b)

while True:
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	plt.ion()
	for boid in boids:
		boid.updateVel(boids)
		boid.updatePos()
		ax.scatter(boid.pos[0],boid.pos[1],boid.pos[2])
	plt.pause(0.0000000001)
		





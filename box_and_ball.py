from vpython import *
import random
import matplotlib.pyplot as plt
a1=random.uniform(-5,5);a2=random.uniform(-5,5);a3=random.uniform(-5,5)
p1=random.uniform(-5,5);p2=random.uniform(-5,5);p3=random.uniform(-5,5)
v1=random.uniform(-5,5);v2=random.uniform(15,25);v3=random.uniform(15,25)
u1=random.uniform(15,25);u2=random.uniform(15,25);u3=random.uniform(15,25)
ball1 = sphere(pos=vector(a1,a2,a3), radius=0.7, color=color.cyan,make_trail=True)
ball2 = sphere(pos=vector(p1,p2,p3), radius=0.8, color=color.red,make_trail=True,trail_color=color.purple)
wallR = box(pos=vector(6,0,0), size=vector(0.2,12,12), color=color.green)
wallL = box(pos=vector(-6,0,0), size=vector(0.2,12,12), color=color.green)
wallT = box(pos=vector(0,6,0), size=vector(12,0.2,12), color=color.blue)
wallD = box(pos=vector(0,-6,0), size=vector(12,0.2,12), color=color.blue)
wallB = box(pos=vector(0,0,-6), size=vector(12,12,0.2), color=color.red)
wallh = box(pos=vector(0,0,6), size=vector(12,12,0.2), opacity=0)

ball1.velocity1 = vector(v1,v2,v3)
ball2.velocity2 = vector(u1,u2,u3)
deltat = 0.0051
vscale = 0.06
v1 = arrow(pos=ball1.pos, axis=vscale * ball1.velocity1, color=color.yellow)
v2 = arrow(pos=ball2.pos, axis=vscale * ball2.velocity2, color=color.yellow)
t = 0
k = 0

#画图

#plt.title('V(t)--t')    #画图
#plt.xlabel('t')
#plt.ylabel('times')
#plt.show()
while t < 20:
    rate(100)
    if ball1.pos.z > (wallh.pos.z-0.6):
        ball1.velocity1.z = -ball1.velocity1.z
    if ball1.pos.z < (wallB.pos.z+0.6):
        ball1.velocity1.z = -ball1.velocity1.z
    if ball1.pos.y < (wallD.pos.y+0.6):
        ball1.velocity1.y = -ball1.velocity1.y
    if ball1.pos.y > (wallT.pos.y-0.6):
        ball1.velocity1.y = -ball1.velocity1.y
    if ball1.pos.x < (wallL.pos.x+0.6):
        ball1.velocity1.x = -ball1.velocity1.x
    if ball1.pos.x > (wallR.pos.x-0.6):
        ball1.velocity1.x = -ball1.velocity1.x
    ball1.pos = ball1.pos + ball1.velocity1*deltat
    t = t + deltat
    v1.pos=ball1.pos
    v1.axis=ball1.velocity1*vscale

    if ball2.pos.z > 5.4:
        ball2.velocity2.z = -ball2.velocity2.z
    if ball2.pos.z < (wallB.pos.z+0.6):
        ball2.velocity2.z = -ball2.velocity2.z
    if ball2.pos.y < (wallD.pos.y+0.6):
        ball2.velocity2.y = -ball2.velocity2.y
    if ball2.pos.y > (wallT.pos.y-0.6):
        ball2.velocity2.y = -ball2.velocity2.y
    if ball2.pos.x < (wallL.pos.x+0.6):
        ball2.velocity2.x = -ball2.velocity2.x
    if ball2.pos.x > (wallR.pos.x-0.6):
        ball2.velocity2.x = -ball2.velocity2.x
    ball2.pos = ball2.pos + ball2.velocity2*deltat
    v2.pos=ball2.pos
    v2.axis=ball2.velocity2*vscale
    v=ball2.pos-ball1.pos
    if (sqrt(v.x*v.x+v.y*v.y+v.z*v.z))<(ball1.radius + ball2.radius):
        m=ball1.velocity1
        ball1.velocity1 = ball2.velocity2
        ball2.velocity2 = m
        k=k+1
    if (k % 2 ==0):
        v1.color=color.yellow
        v2.color=color.yellow
    else:
        v1.color=color.magenta
        v2.color=color.magenta

    #画图
 #   plt.plot(t,k,'b-',label='V',markersize=0.5)

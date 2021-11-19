from vpython import *
canvas(background=color.purple)
donut=ring(radius=0.5,thickness=0.25,color=vector(400,100,1))
choco=ring(radius=0.6,thickness=0.25,color=vector(0.4,0.2,0))
radian=0
while True:
    rate(20)
    donut.pos=vector(3*cos(radian),sin(radian),0)
    choco.pos=vector(3*cos(radian),sin(radian),0)
    #donut.rotate(angle=radian,axis=vector(0,1,0))
    #choco.rotate(angle=radian,axis=vector(0,1,0))
    radian=0.05+radian
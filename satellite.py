import pgzrun
import random 
import time
WIDTH=800
HEIGHT=600
satellites=[]
lines=[]
nextSatellite=0
startTime=0
endTime=0
totalTime=0
numSatellites=10
def create():
    global startTime
    for i in range(0,numSatellites):
        sat=Actor('satellite')
        sat.pos=random.randint(40,WIDTH-40),random.randint(40,HEIGHT-40)
        satellites.append(sat)
        startTime=time.time()
def draw():
    global totalTime
    screen.blit('starsbg.png',(0,0))
    number=1
    for sat in satellites:
        screen.draw.text(str(number),(sat.pos[0],sat.pos[1]+20))
        sat.draw()
        number=number+1
    for line in lines:
        screen.draw.line(line[0],line[1],(255,255,255))
    if nextSatellite<numSatellites:
        totalTime=time.time()-startTime
        screen.draw.text(str(round(totalTime,1)),(10,10),fontsize=30)
    else:
        screen.draw.text(str(round(totalTime,1)),(10,10),fontsize=30)

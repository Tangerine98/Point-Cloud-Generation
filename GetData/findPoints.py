import serial
import numpy

port = input("Enter port : ")

ser = serial.Serial('/dev/ttyACM0',9600)

l = 10
r = 10
BaseTurns = 86
LinkTurns = BaseTurns
singlePhi = (360/BaseTurns)
singleTheta = (180/LinkTurns)
distanceFromFloor = 0
noOfPoints = BaseTurns*LinkTurns
phi = 0
theta = 0

f = open("points.pcd","w")

f.write("# .PCD v0.7 - Point Cloud Data file format\n")
f.write("VERSION 0.7\n")
f.write("FIELDS x y z\n")
f.write("SIZE 4 4 4\n")
f.write("TYPE F F F\n")
f.write("COUNT 1 1 1\n")
f.write("WIDTH "+ str(noOfPoints) +"\n")
f.write("HEIGHT 1\n")
f.write("VIEWPOINT 0 0 0 1 0 0 0\n")
f.write("POINTS "+ str(noOfPoints) +"\n")
f.write("DATA ascii\n")

for i in range (0, BaseTurns) :
    for j in range (0, LinkTurns) :
        phi += singlePhi
        theta += singleTheta
        distance = ser.read(4)      #Size of dimension (of data received) is 4 bytes
        x = (r+distance)*numpy.cos(theta)*numpy.sin(phi)
        y = l + distanceFromFloor + (r+distance)*numpy.sin(theta)
        z = (r+distance)*numpy.cos(theta)*numpy.cos(phi)
        f.write(str(x)+" "+str(y)+" "+str(z)+"\n")

f.close()
import numpy
import serial
import struct
import tkinter as tk

l = 10
r = 10

#arduino = serial.Serial('/dev/ttyACM2', 9600) # Establish the connection on a specific port

top = tk.Tk()
top.title("Two-Joint Robotic Arm")

xLabel = tk.Label(top,text="Enter x : ")
xLabel.grid(column=0,row=0)
xValue = tk.Entry(top)
xValue.grid(column=1,row=0)

yLabel = tk.Label(top,text="Enter y : ")
yLabel.grid(column=0,row=1)
yValue = tk.Entry(top)
yValue.grid(column=1,row=1)

zLabel = tk.Label(top,text="Enter z : ")
zLabel.grid(column=0,row=2)
zValue = tk.Entry(top)
zValue.grid(column=1,row=2)

def callback() :
	x = float(xValue.get())
	y = float(yValue.get())
	z = float(zValue.get())
	if ( y>=l) :
		if ( r >= numpy.sqrt(x**2 + (y-l)**2 + z**2)) :
			printLabel = tk.Label(top,text="Point is on the Surface")
			printLabel.grid(column=0, row=4)
			theta = numpy.degrees(numpy.arcsin((y-l)/r))
			phi = numpy.degrees(numpy.arctan(z/x))
			thetaValue = "Theta = "+str(theta)
			phiValue   = "Phi   = "+str(phi)
			thetaLabel = tk.Label(top, text=thetaValue)
			thetaLabel.grid(column=0,row=5)
			phiLabel = tk.Label(top, text=phiValue)
			phiLabel.grid(column=1, row=5)
			#arduino.write(struct.pack('>BB',int(theta),int(phi)))
			#arduino.write(struct.pack('>B',int(phi)))
		else :
			printLabel = tk.Label(top,text="Point not on the surface")
			printLabel.grid(column=0, row=4)
	else :
		printLabel = tk.Label(top,text="y < l")
		printLabel.grid(column=0, row=4)

values = tk.Button(top,text="Enter",command=callback)
values.grid(column=1,row=3)

top.mainloop()

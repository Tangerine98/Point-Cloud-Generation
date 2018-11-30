#Point Cloud Generation
This project uses a arduino and python(3.x) to generate a PCD file from the arduino and visualize it in VTK.
This is done in 2 steps
1. Createing the PCD file by getting data from the Arduino
2. Visualize the PCD file

##Prerequisites

This project uses Python 3.x, pip and Arduino IDE.

* [Arduino IDE] (https://www.arduino.cc/en/Guide/Linux) - Instruction to install arduino ide in linux
Installing python and pip
###Debain based systems
'''
apt install python3 python3-pip
'''
###Arch based systems
'''
pacman -S pyhton pyhton-pip
'''
##Installing
External packages used in the python program are: `Numpy`,`VTK`,`PySerial`
These can be install manually or by using the included requirments.txt in the root of this project 
###Debain based systems
'''
pip3 install -r requirements.txt
'''

###Arch based systems
'''
pip install -r requirements.txt
'''

##How to use this project?

###Arduino code
The arduino code is located in the `SweepBoth` folder. Flash `SweepBoth.ino` located in that file to the Arduino

###Gnerating the PCD 

Connecte your arduino and then run the following commands
'''
cd GetData
python findpoints.py
'''

###Visualize the PCD file

Copy the Generated points.pcd into `GeneratePointCloud` and run
'''
cd GeneratePointCloud
python pointscloud.py points.pcd
'''

##Presentation and Report
The report and presentation are created using latex these are located in 
```./presentation``` and ```./report```
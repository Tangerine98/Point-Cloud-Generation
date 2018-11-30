import serial
import numpy
import time
import os
import serial.tools.list_ports


def get_arduino_port():
    ports_list = list(serial.tools.list_ports.comports())
    if ports_list:
        for p in ports_list:
            device = str(p.description)
            if "ACM" in device:
                arduino_port = "/dev/" + device
                return arduino_port
            else:
                print("Arduino not found.\n")
    else:
        print("no device not found.\n")


def find_position(distance, phi, theta):
    x = (link1_length + distance) * numpy.cos(theta) * numpy.sin(phi)
    y = base_link_length + distanceFromFloor + \
        (link1_length + distance) * numpy.sin(theta)
    z = (link1_length + distance) * numpy.cos(theta) * numpy.cos(phi)
    return x, y, z


def data_parser(raw_data):
    parameters = raw_data.split(',')
    dist = float(parameters[0])
    phi = float(parameters[1])
    theta = float(parameters[2])
    print("distance:" + str(dist) + "\t" + " phi:" +
          str(phi) + "\t" + " theta:" + str(theta) + "\n")
    return dist, phi, theta


if __name__ == "__main__":

    # length of links in cm
    base_link_length = 20
    link1_length = 19.5
    BaseTurns = 22  # 110/5 check ino file
    LinkTurns = 62  # 155/5 *2 check ino file
   #singlePhi = (360/BaseTurns)
    #singleTheta = 10
    distanceFromFloor = 0
    noOfPoints = BaseTurns * LinkTurns
    zero_value_points = 0
    maxrange_value_points = 0
    no_of_points = 0
    pcd_file = "points"

    port = get_arduino_port()
    print("Arduino found in " + port)
    print("connecting")
    ser = serial.Serial(port, 9600)

    # to check if file exist if it does add numbering to file
    if(os.path.isfile(pcd_file+".pcd")):
        pcdfile = pcd_file
        for i in range(1, 100):
            if(os.path.isfile(pcdfile+".pcd")):
                pcdfile = pcd_file+"_"+str(i)+".pcd"
            else:
                break

    # open file and initilize pcd values
    f = open(pcdfile, "w")
    f.write("# .PCD v0.7 - Point Cloud Data file format\n")
    f.write("VERSION 0.7\n")
    f.write("FIELDS x y z\n")
    f.write("SIZE 4 4 4\n")
    f.write("TYPE F F F\n")
    f.write("COUNT 1 1 1\n")
    f.write("WIDTH " + str(noOfPoints) + "\n")
    f.write("HEIGHT 1\n")
    f.write("VIEWPOINT 0 0 0 1 0 0 0\n")
    f.write("POINTS " + str(noOfPoints) + "\n")
    f.write("DATA ascii\n")

    for i in range(0, BaseTurns):
        for j in range(0, LinkTurns):
            time.sleep(1)
            ser.flushInput()
            # while ser.in_waiting :
            raw_distance = ser.readline()
            distance, phi, theta = data_parser(raw_distance.decode())

            # TO check if points are in range
            if distance == 0.0:
                zero_value_points = zero_value_points + 1
                print("No of zero points:" + str(zero_value_points))
            elif distance > 450.00:
                maxrange_value_points = maxrange_value_points + 1
                print("No of points above range:" + str(maxrange_value_points))

            else:
                x, y, z = find_position(distance, phi, theta)
                print("x:" + str(x) + " y:" + str(y) + " z:" + str(z) + "\n")
                f.write(str(x)+" "+str(y)+" "+str(z)+"\n")
            no_of_points = no_of_points + 1
            print("total no of points:" + str(no_of_points)+"\n")

    f.close()
    print("PCD file generated")
    print("Ratio(zero/total):" + str(zero_value_points/no_of_points))
    print("Ratio(maxvalue/total):" + str(maxrange_value_points/no_of_points))

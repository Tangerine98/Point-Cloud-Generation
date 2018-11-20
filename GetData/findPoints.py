import serial,numpy,time
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

        
        

def find_position(distance,phi,theta):
    x =  (link1_length + distance) * numpy.cos(theta) * numpy.sin(phi)
    y = base_link_length + distanceFromFloor + (link1_length + distance) * numpy.sin(theta)
    z = (link1_length + distance) * numpy.cos(theta) * numpy.cos(phi)
    return x,y,z


def data_parser(raw_data):
    parameters = raw_data.split(',')
    print(parameters)
    dist = float(parameters[0])
    phi = float(parameters[1])
    theta = float(parameters[2])
    print("distance:" + str(dist) + " phi:" + str(phi) + " theta:" + str(theta) + "\n")
    return dist,phi,theta
    


if __name__ == "__main__":

    #length of links in cm
    base_link_length = 20 
    link1_length = 19.5
    BaseTurns = 7 #10000 
    LinkTurns = 38 #10000 
    singlePhi = (360/BaseTurns)
    singleTheta = 10
    distanceFromFloor = 0
    noOfPoints = BaseTurns * LinkTurns

    port = get_arduino_port()
    print("Arduino found in " + port)
    print("connecting")
    ser = serial.Serial(port,9600)


    #open file and initilize pcd values
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


    for i in range (0, BaseTurns):
        for j in range (0, LinkTurns):
            #phi += singlePhi
            #theta += singleTheta
            time.sleep(1)
            ser.flushInput()
            #while ser.in_waiting :
            raw_distance = ser.readline()
            #raw_distance = ser.read(10)
            distance,phi,theta = data_parser(raw_distance.decode())
            #distance = float(raw_distance.decode())
            #print(distance)
            x,y,z = find_position(distance,phi,theta)
            print("phi: " + str(phi) + " theta: " + str(theta))
            print("x:" + str(x) + " y:" + str(y) + " z:" + str(z) + "\n")
            f.write(str(x)+" "+str(y)+" "+str(z)+"\n")
            print("i:" + str(i) + "j:" + str(j))

    print("PCD file generated")
    f.close()
import serial



# print("ss")
921.6
serialComm = serial.Serial('/dev/ttyUSB0', 9600, timeout=None)
print(serialComm.name)
serialComm.write("R")
# serialComm.flush()
rx = serialComm.read(size=27)
print(rx)
serialComm.close()
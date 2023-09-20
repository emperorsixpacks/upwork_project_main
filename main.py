import sys
import time
import serial
import serial.tools.list_ports as ports
from serial.serialutil import SerialException



def main():
    input_com = serial.Serial("COM1") #This works only on windows, Linux use ttyUSBx
    output_com = serial.Serial("COM2")
    com_ports = ports

    print("All COM ports")
    for com,name,pair in com_ports.comports():
        print(com) # We are printing all available COM ports here

    input_com.baudrate = 9600 # Setting the baudrate to 960
    output_com.baudrate = 9600

    count = 0 # This is just a cunter, it doesn't affect our code so much, it just helps us keep track of our output
    
    print("PROGRAM BGEIN")
    while True:
        input_com.write(f"This is from the input COM...... count is: {count}".encode()) # We write to COM 1
        time.sleep(1) # Sleep for one second
        print(output_com.read_all()) # We print the output from COM 2
        count+=1 # We increament the counter by one
    
    
if __name__ == "__main__":
    try:
        main()
    except SerialException:
        print("No COM port found")
    except KeyboardInterrupt:
        print("Program closed")
#-*- coding :utf-8 -*-
import serial
import time
from time import sleep
def main():
    ser =serial.Serial('/dev/arduino',9600,timeout=1)
    sleep(1.5)
    prev_data=''
    while True:
        #starttime =time.time()
        try:
            f = open('matrixSpecialFile.txt','r')
            data =f.read()
            f.close()
        except:
            print("err")

        try:
            if(data != prev_data):
                ser.write(data)
                sleep(1.5)
                prev_data=data
                print str(data)
                #endtime = time.time()
                #intervel = endtime - starttime
                #print(str(interval)+"s:"+str(data))
        except:
            print("err:"+str(data))
    ser.close()

if __name__ == '__main__':
    main()

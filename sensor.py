import RPi.GPIO as GPIO
import dht11
import serial
import time
import datetime
import sys

# set serial
ser = serial.Serial(
        '/dev/ttyUSB0',
        baudrate = 9600,
        parity = serial.PARITY_NONE,
        stopbits = serial.STOPBITS_ONE, 
        bytesize = serial.EIGHTBITS,
        timeout = 1)

# initalize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

def get_dht11(pin):
    instance = dht11.DHT11(pin)
    result = instance.read()
    if result.is_valid():
        return result
    else:
        print 'fail'


def get_moisture(ser):
    try:
        data = ''
        while(data == ''):
            data = ser.readline(ser.inWaiting())
        return data
    except:
        print 'fail'

def main():
    #pin = int(sys.argv[1])
    pin = 14
    dht_result = get_dht11(pin)
    moisture = get_moisture(ser)
    time.sleep(0.5)
    date = str(datetime.datetime.now())
    sensor = str(dht_result.temperature) + "," + str(dht_result.humidity) 
    sensor += "," + str(moisture)
    print date
    print sensor


if __name__ == '__main__':
    main()


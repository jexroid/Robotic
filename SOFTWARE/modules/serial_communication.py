import time
import serial
from serial import Serial

class communicate:
    # lets make ser global cuase we need it every where
    global ser , ser2
    # ser variable ( the laws of communication )
    ser = serial.Serial(
            port='/dev/ttyUSB1',
            baudrate = 9600,
            timeout = 1.0
        )
    # wait a little for better recengization
    time.sleep(3)
    # clear the buffer
    ser.reset_input_buffer()


    ser2 = serial.Serial(
            port='/dev/ttyUSB0',
            baudrate = 9600,
            timeout = 1.0
        )
    # wait a little for better recengization
    time.sleep(3)
    # clear the buffer
    ser2.reset_input_buffer()

    def send(message):
        ser.write(f"{message} !\n".encode('utf-8'))

    def listener():
        try:
            while ser.in_waiting <= 0:
                time.sleep(0.01)
            responser = ser.readline().decode('utf-8').rstrip()
            print(responser)
        except KeyboardInterrupt:
            print("closing the communication")

        return responser

    def stop():
        ser.close()

    def send2(message):
        ser2.write(f"{message} !\n".encode('utf-8'))
    def listener2():
        try:
            while ser2.in_waiting <= 0:
                time.sleep(0.01)
            responser = ser2.readline().decode('utf-8').rstrip()
            print(responser)
        except KeyboardInterrupt:
            print("closing the communication")

        return responser
    def stop2():
        ser2.close()

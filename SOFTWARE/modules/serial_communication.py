import time
import serial
from serial import Serial

class communicate:
    def start():
        # lets make ser global cuase we need it every where
        global ser

        # ser variable ( the laws of communication )
        ser = serial.Serial(
                port='/dev/ttyS0',
                baudrate = 9600,
                timeout = 1.0
            )

        # wait a little for better recengization
        time.sleep(3)

        # clear the buffer
        ser.reset_input_buffer()


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
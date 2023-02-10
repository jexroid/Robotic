import cv2 as cv
import numpy as np
from modules import color
from modules import serial_communication as sc


def main():
    cap = cv.VideoCapture(0)
    while (True):
        _, frame = cap.read()

        # detecting the color of the object
        color_of_object = color.detect_color(frame)
        return color_of_object


# start the communication
sc.communicate.start()

# wait for hardware , then main work will be started

print("waiting ...")
while (True):
    response = sc.communicate.listener()

    if response == "color":
        print(response)
        # run the color detection
        color_of_object = main()

        print(color_of_object, "is the color of object")
        sc.communicate.send(color_of_object)

        print(color_of_object, "has sended to HARDWARE")
        break

    print("the job is done")
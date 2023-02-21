import cv2 as cv
import numpy as np
from modules import movement_wight as mw
from modules import movement_hight as mh
from modules import serial_communication as sc

mh.detect()
mw.detect()


# start the communication
sc.communicate.start()

# wait for hardware , then main work will be started

print("waiting ...")
while True:
    response = sc.communicate.listener()

    if response == "color":
        print(response)
        # run the color detection

        # print(color_of_object, "is the color of object")
        # sc.communicate.send(color_of_object)

        # print(color_of_object, "has sended to HARDWARE")
        break
        
    print("the job is done")
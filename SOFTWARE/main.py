from time import sleep
from gpiozero import AngularServo
from modules import movement_wight as mw
from modules import movement_hight as mh
from modules import serial_communication as sc
from modules import text
from colorama import Fore


going_to_shelf = ["x,0.56", "y,0.56", "x,0.6",
                  "y,-0.11", "y,0.11", "x,-0.6", "y,-0.56", "x,-0.56"]
shelf_returning_to_start_point = ["y,0.4"]
paper_in_room_one = []
returning_from_room_one_to_start_point = []
paper_in_room_tow = []
paper_in_room_three = []
paper_in_room_four = []


def moving(List):
    for i in List:
        pashmak = i
        print(pashmak)
        sc.communicate.send(pashmak)
        while True:
            HARDWARE = sc.communicate.listener()
            if HARDWARE == 'ok':
                break


# moving(going_to_shelf)


# servo = AngularServo(17 , min_pulse_width=0.0006 , max_pulse_width=0.0023)
# servo.angle =  0
# moving(going_to_shelf)

sc.communicate.send2("00")

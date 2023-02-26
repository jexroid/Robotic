from time import sleep
from modules import y
from modules import x
from modules import serial_communication as sc
from modules import text
from modules import bazo
from colorama import Fore


def moving(List):
    for i in List:
        pashmak = i
        print(pashmak)
        sc.communicate.send(pashmak)
        while True:
            HARDWARE = sc.communicate.listener()
            if HARDWARE == 'ok':
                break


going_to_shelf = []
shelf_returning_to_start_point = []
room_one = ["x,0.56", "y,0.56", "x,0.6","y,-0.11", "y,0.11", "x,-0.6", "y,-0.56", "x,-0.56"]
paper_in_room_one = []
returning_from_room_one_to_start_point = []
paper_in_room_tow = []
paper_in_room_three = []
paper_in_room_four = []



# moving(going_to_shelf)

bazo.mid()


# thing for tommarow 

# matplot lib and object color and how pixel and how bazo should react
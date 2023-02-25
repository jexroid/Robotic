from time import sleep
from modules import bazo
from modules import x
from modules import serial_communication as sc
from modules import text
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


going_to_shelf = ["x,0.56", "y,0.56", "x,0.6",
    "y,-0.11", "y,0.11", "x,-0.6", "y,-0.56", "x,-0.56"]
shelf_returning_to_start_point = ["y,0.4"]
paper_in_room_one = []
returning_from_room_one_to_start_point = []
paper_in_room_tow = []
paper_in_room_three = []
paper_in_room_four = []


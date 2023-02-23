from modules import movement_wight as mw
from modules import movement_hight as mh
from modules import serial_communication as sc
from colorama import Fore



going_to_shelf = ["y,-0.5", "x,+.0.3", "y,-0.4"]
shelf_returning_to_start_point = []
paper_in_room_one = []
returning_from_room_one_to_start_point = []
paper_in_room_tow = []
paper_in_room_three = []
paper_in_room_four = []

def moving(List):
    for i in List:
        pashmak = i
        sc.communicate.send(pashmak)
        while True:
            HARDWARE = sc.communicate.listener()
            if HARDWARE == 'ok':
                break

moving(going_to_shelf)
# wait for hardware , then main work will be started

# print("waiting ...")
# while True:
#     response = sc.communicate.listener()
#     print(Fore.RED,"HARDWARE SAYS : ", response , Fore.WHITE)
#     if response == "move":
#         mh.detect()
#         # run the color detection

#         # print(color_of_object, "is the color of object")
#         # sc.communicate.send(color_of_object)

        
#         break
        
#     print("the job is done")
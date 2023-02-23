from modules import serial_communication as sc


going_to_shelf = ["y50", "x-30", "y-15"]
sc.communicate.send(going_to_shelf)
sc.communicate.listener("ok")
shelf_returning_to_start_point = []
paper_in_room_one = []
returning_from_room_one_to_start_point = []
paper_in_room_tow = []
paper_in_room_three = []
paper_in_room_four = []

for i in range(len(going_to_shelf)):
    pashmak = going_to_shelf[i]
    sc.communicate.send(pashmak)
    while (sc.communicate.listener('ok')):
        break
    ["y,50", "x,-50", "y,-50", "x,50"]

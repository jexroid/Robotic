from modules import serial_communication as sc

def min():
    sc.communicate.send_bazo("1")

def mid():
    sc.communicate.send_bazo("2")
def max():
    sc.communicate.send_bazo("3")


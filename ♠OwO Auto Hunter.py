from pynput.keyboard import Key, Controller
import time
import random
import os


keyboard = Controller()

def auto_hunt():
     
     
     keyboard.press('o')
     keyboard.release('o')
     
     keyboard.press('w')
     keyboard.release('w')
     
     keyboard.press('o')
     keyboard.release('o')
     
     keyboard.press(Key.space)
     keyboard.release(Key.space)
     
     keyboard.press('h')
     keyboard.release('h')
     
     keyboard.press(Key.enter)
     keyboard.release(Key.enter)
     
def things():
    os.system("cls")
    print("      OwO Auto Hunter By ♠D3mon♠")
    print("♠  Version:- 1.0")
    print("* youtube.com/@d3mon69")
    print("")
    print("")
    print("")
    print("")



def ran_n():
    a = 15
    b = 20
    global num
    num = random.randint(a, b)


def main():
    print("Repeat Times :         ")
    n = int(input())
    print('Ｒｕｎｎｉｎｇ...')
    time.sleep(5)
    i = int(0)
    while i < n:
        auto_hunt()
        time.sleep(num)
        i += 1


things()
ran_n()
main()

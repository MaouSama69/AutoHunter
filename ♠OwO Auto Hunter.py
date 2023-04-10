from pynput.keyboard import Key, Controller
import time
import random
import os


keyboard = Controller()
def auto_s():
     keyboard.press('o')
     keyboard.release('o')
     
     keyboard.press('w')
     keyboard.release('w')
     
     keyboard.press('o')
     keyboard.release('o')

     keyboard.press(Key.space)
     keyboard.release(Key.space)
     
     keyboard.press('s')
     keyboard.release('s')

     keyboard.press(Key.enter)
     keyboard.release(Key.enter)



def auto_flip():
     keyboard.press('o')
     keyboard.release('o')
     
     keyboard.press('w')
     keyboard.release('w')
     
     keyboard.press('o')
     keyboard.release('o')

     keyboard.press(Key.space)
     keyboard.release(Key.space)

     keyboard.press('c')
     keyboard.release('c')
     
     keyboard.press('f')
     keyboard.release('f')

     keyboard.press(Key.space)
     keyboard.release(Key.space)

     keyboard.press('1')
     keyboard.release('1')

     keyboard.press(Key.enter)
     keyboard.release(Key.enter)


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
        time.sleep(2)
        auto_s()
        time.sleep(2)
        auto_flip()
        time.sleep(num)
        i += 1


things()
ran_n()
main()

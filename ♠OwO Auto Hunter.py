from pynput.keyboard import Key, Controller
import time
import random
import os

keyboard = Controller()

# Function to simulate key presses
def press_keys(*keys):
    for key in keys:
        keyboard.press(key)
        keyboard.release(key)
        time.sleep(0.1)

def auto_s():
    press_keys('o', 'w', 'o', Key.space, 's', Key.enter)

def auto_coin_flip():
    press_keys('o', 'w', 'o', Key.space, 'c', 'f', Key.space, '6', '9', Key.enter)

def auto_hunt():
    press_keys('o', 'w', 'o', Key.space, 'h', Key.enter)

def display_info():
    os.system("cls" if os.name == "nt" else "clear")
    print("\t\tAuto Hunter By D3mon")
    print("♠  Version:- 2.0")
    print("* youtube.com/@d3mon69")
    print("\n" * 3)

def get_random_delay():
    return random.randint(15, 20)

def get_valid_repeat_count():
    while True:
        try:
            n = int(input("Repeat Times (max 35): "))
            if n > 35:
                print("Please enter a number 35 or below.")
            elif n <= 0:
                print("Please enter a positive number.")
            else:
                return n
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def main():
    display_info()
    n = get_valid_repeat_count()

    print("Ｒｕｎｎｉｎｇ...")
    time.sleep(3)

    for i in range(n):
        auto_hunt()
        time.sleep(2)
        auto_s()
        time.sleep(2)
        auto_flip()
        time.sleep(get_random_delay())

    print("Automation Complete!")

if __name__ == "__main__":
    main()

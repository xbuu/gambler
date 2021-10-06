import random
import time
import os

print('''
------------------
     gambler
------------------
suggested by henry
''')
money = 500

def gambler():
    print(f"Current Balance: {money}")
    gamble = int(input("Enter the money you want to gamble: "))
    winorlose = ["ya win", "ya lose"]

    win = random.choice([True, False])

    if gamble >= money:
        os.system("cls")
        print("YOU LOSE!!!")
        print("lmao idiot u gambled too much")
        time.sleep(2)
    else:
        os.system("cls")
        if win == False:
            print("you lost")
            result = money-gamble
            print(result)
        else:
            print("you won")
            result = money+gamble
            print(result)
        gambler()

gambler()
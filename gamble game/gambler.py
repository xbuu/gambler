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
    gamble = int(input("Enter the money you want to gamble: "))
    winorlose = ["ya win", "ya lose"]

    win = random.choice([True, False])

    if gamble >= money:
        os.system("cls")
        print("You lost the gamble.")
        print('-------------------')
        result = money - gamble
        print("Current Balance is:")
        print(result)
        print('-------------------')
        print("You gambled a little \ntoo much.")
        time.sleep(5)
    else:
        os.system("cls")
        if win == False:
            print("You lost the gamble.")
            print('-------------------')
            result = money-gamble
            print("Current Balance is:")
            print(result)
        else:
            print("You won the gamble!")
            print('-------------------')
            result = money+gamble
            print("Current Balance is:")
            print(result)
        gambler()

gambler()
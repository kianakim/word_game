# main.py
# Author: Kiana Kim

# tl;dr when you click randomly you get words you can spend to make silly phrases
import random

fnoun = open("nounlist.txt", "r")
fsave = open("saved.txt", "a")

# spin for word
while True:
    fsave = open("saved.txt", "a")
    enter = input("Hit ENTER to spin (or type Q to exit game) ")

    # QUIT GAME
    if enter == "Q":
        fsave.close()
        print("GAME OVER... for now")
        exit()

    number = random.randint(1, 3)

    # you won a word
    if number == random.randint(1,3):
        line_num = random.randint(1,1000)
        for x in range (1, line_num):
            fnoun.readline()
        word = fnoun.readline().rstrip()
        print(repr(word)+ "\n")

        while True:
            save_input = input("!! SAVE? (Y/N): ")
            if save_input == 'Y':
                fsave.write(word)
                fsave.write("\n")
                fsave.close()
                print("saved\n")
                break
            elif save_input == 'N':
                print("not saved\n")
                break
            else:
                print("Invalid Option\n")

    # didnt win a word
    else:
        print("NO WORD THIS TIME :(\n")
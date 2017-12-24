# mainMenu.py
# Author: Kiana Kim

print("   My Word Game\n  By: Kiana Kim\n")

# Enter save name
fprofiles =  open("savedProfiles.txt", "a")
intro = 0
new_profile = 0

while intro == 0:
    name = input("Enter save name: ")

    if name in open("savedProfiles.txt").read():
        print("Welcome back, " + name)
        break
    elif name == "Q":
        print("Goodbye!")
        exit()
    else:
        while True:
            new_save = input("Create a new save file? (Y/N)")
            if new_save == 'Y':
                fprofiles.write(name + "\n")
                fprofiles.close()
                print("New Profile Saved. Welcome, " + name + "\n")
                new_profile = 1
                intro = 1
                break
            elif new_save == 'N':
                break
            else:
                print("Invalid Option\n")

print("Enter '1' to view your saved words")
print("Enter '2' to spin for new words")
print("Enter '3' to put words together")
menu  = input("")

if menu == '1':
    print("go to word-viewing UI")
elif menu == '2':
    print("go to spin UI")
elif menu == '3':
    print("go to word put together UI")
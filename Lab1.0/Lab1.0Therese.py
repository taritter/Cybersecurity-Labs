"""
Cybersecurity Lab 1.0
Therese (Tess) Ritter
CS2660OL / Spring 2024

This is a program to log in to a spy companies intranet system
"""

import csv


file = open('Spy_Data.csv')

spy = [1,4,5,6]
tech = [1,2,4,5]
admin = [1,2,3,4,5,6]


user = input("Enter your username: ")
user_pw = input("Enter your password: ")

accepted = False
valid = False

for line in file:
    info = line.split(",")
    if user == info[0] and user_pw == info[1]:
        accepted = True
        level = int(info[2].strip('\n'))
        if level == 1:
            employee = spy
        elif level == 2:
            employee = tech
        else:
            employee = admin
        print("Welcome " + user + ", you now have access to SpyHub")
        while not valid:
            try:
                menu = int(input("Choose a number selection from the menu:\n1. Profile\n2. Police Data\n3. Admin\n4. Weapons\n5. Blueprints/Maps\n6. Assignments\n\n"))
                if menu not in employee and menu not in range(1,6):
                    print("Not a valid option.")
                elif menu not in employee and menu in range(1,6):
                    print("You are not authorized to access this area.\n")
                    back = input("Type 'r' to go back, type 'q' to leave\n")
                    if back == 'q':
                        valid = True
                elif menu in employee:
                    valid = True
                    if menu == 1:
                        print("You now have access to spy profile")
                    elif menu == 2:
                        print("You now have access to police data")
                    elif menu == 3:
                        print("Welcome, you now have admin access")
                    elif menu == 4:
                        print("You now have access to weapons")
                    elif menu == 5:
                        print("You now have access to blueprints/maps")
                    else:
                        print("You now have access to previous and current assignments")
            except ValueError:
                print("Not a valid option.")

if accepted == False:
    print("Invalid user")

file.close()



#account info for a spy
#user 1 is the spy and they see their assignments, weapons, profile
#user 2 is the spy's technical assistant they see weapons, profile, blueprints/maps, person lookup, police
#user 3 is the supervisor and they look at everything

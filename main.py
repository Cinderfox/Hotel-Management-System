import os
from random import randint

rooms = {}
customers = {}
reviews = {}

def input_room():
    n = int(input("Enter the number of rooms to be entered: "))
    for _ in range(n):
        room = input("Enter the room number: ")
        size = input("Enter the room size: ")
        status = input("Enter the room availability (AVAILABLE/BOOKED): ")
        cost = float(input("Enter the room cost in dlr/night: "))
        rooms[room] = {
            'size': size,
            'status': status,
            'cost': cost
        }
    print("Rooms have been successfully entered.\n")
    
def delete_room():
    room_delete = input("Enter the room number to be deleted: ")
    if room_delete in rooms:
        del rooms[room_delete]
        print("Room has been deleted.\n")
    else:
        print("Room not found.\n")


def edit_room():
    room_edit = input("Enter the room number to be edited: ")
    if room_edit in rooms:
        while True:
            print("\n1. Edit size")
            print("2. Edit status")
            print("3. Edit cost")
            print("4. Exit edit")
            ch = input("Enter your choice: ")
            
            if ch == '1':
                new_size = input("Enter new size: ")
                rooms[room_edit]['size'] = new_size
                print("Successfully edited.\n")
            elif ch == '2':
                print("1. AVAILABLE")
                print("2. BOOKED")
                E = input("Enter your choice: ")
                if E == '1':
                    rooms[room_edit]['status'] = 'AVAILABLE'
                    print("Successfully edited.\n")
                elif E == '2':
                    rooms[room_edit]['status'] = 'BOOKED'
                    print("Successfully edited.\n")
                else:
                    print("Invalid choice.\n")
            elif ch == '3':
                new_cost = float(input("Enter new cost in dhs/night: "))
                rooms[room_edit]['cost'] = new_cost
                print("Successfully edited.\n")
            elif ch == '4':
                break
            else:
                print("Invalid choice.\n")
    else:
        print("Invalid room.\n")

def main_menu():
    print("""
                                        .........................................
                                        \\\\\\\\WELCOME TO SEVEN SEAS GRAND HOTEL////
                                        .........................................
    """)
    while True:
        print("\nHOTEL MANAGEMENT SYSTEM")
        print("1. Check-in")
        print("2. Check-out")
        print("3. Admin")
        print("4. Review")
        print("5. View Reviews")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            check_in()
        elif choice == '2':
            check_out()
        elif choice == '3':
            admin_menu()
        elif choice == '4':
            review()
        elif choice == '5':
            view_reviews()
        elif choice == '6':
            break
        else:
            print("Invalid choice.\n")

main_menu()
import os
from random import randint
print("""
                                      .................................................
                                      \\\\\\\\WELCOME TO SEVEN SEAS GRAND HOTEL////////
                                      .................................................
""")
rooms=dict()
customer=dict()
reviews=dict()
reviews['NAME']=('REVIEW')
def input_room():
    os.system('cls')
    n=int(input("enter the number of rooms to be entered"))
    for i in range(n):
        room=input("enter the room number")
        det=eval(input("enter the details in the form [size,status,cost(in dhs/night)]-"))
        rooms[room]=det
    print ("rooms have successfully been entered\n")

def delete_room():
    os.system('cls')
    room_delete=input("enter the room number to be deleted")
    x=rooms.pop(room_delete,"none")
    if x=="none":
        print("room not found\n")
    else:
        print("deleted\n")

def edit_room():
    os.system('cls')
    room_edit=input("enter room number to be edited\n")
    q=rooms.keys()
    if room_edit in q:
        while True:
            print("\n1-edit size")
            print("2-edit status")
            print("3-edit cost")
            print("4-exit edit\n")

            ch=input("enter your choice-")

            if int(ch)==1:
                new_size=input("enter new size")
                rooms[room_edit][0]=new_size
                print("successfully edited\n")
            elif int(ch)==2:
                print("1-AVAILABLE")
                print("2-BOOKED")
                E=int(input("enter your choice"))
                if E==1:
                    rooms[room_edit][1]='AVAILABLE'
                    print("successfully edited\n")
                elif E==2:
                    rooms[room_edit][1]='BOOKED'
                    print("successfully edited\n")
                else:
                    print("invalid choice\n")
            elif int(ch)==3:
                new_cost=input("enter new cost in dhs/night")
                rooms[room_edit][2]=new_cost
                print("successfully edited\n")
            elif int(ch)==4:
                break
            elif int(ch)=="":
                print("Please enter a choice\n")
            else:
                print("invalid choice\n")
    else:
        print("invalid room\n")


def show_rooms():
    os.system('cls')
    L=rooms.keys()
    print("Room number\t\tSize\t\tAvailability\t\tCost")
    for i in L:
        print("        ",i,end="\t            ")
        for j in range(3):
            print (rooms[i][j],end="\t              ")       
        print()
    print("\n")

def check_in():
    os.system('cls')
    name=input("Enter your name")
    while True:
        room=input("Enter the room number you would like to book-")
        Q=rooms.keys()         
        if room in Q:
            if rooms[room][1]=="BOOKED":   
                print("This room is booked. Please choose another room.\n")
            if rooms[room][1]=="AVAILABLE":
                rooms[room][1]="BOOKED"  
                print("The room has been booked.\n")
                break
        else:
            print("Please enter a valid room number.\n")
    phone_no=input("Enter your mobile number")
    address=input("enter your address")
    check_in=input("Enter check in date and time (in format DD-MM-YYYY,HH:MM)-")
    check_out="  -   "
    customer[name]=([room,phone_no,address,check_in,check_out])


def check_out():
    os.system('cls')
    Q=customer.keys()
    name=input("enter  your name")
    print("room number=",customer[name][0])
    print("phone number=",customer[name][1])
    print("address=",customer[name][2])
    print("check in date and time=",customer[name][3])
    check_out=input("enter check out date and time (in format DD-MM-YYYY,HH:MM)-")
    customer[name][4]=check_out
    nights=int(input("Enter number of nights stayed"))
    tot_food=randint(0,200)
    tot_bev=randint(0,200)
    tot_room=randint(0,100)
    total_cost= tot_food+tot_bev+tot_room+nights*rooms[customer[name][0]][2]
    print("\n                                                BILL")
    print("                               SEVEN SEAS GRAND HOTEL")
    print("                                        ",customer[name][4] )
    print("******************************************************************************")
    print("                            TOTAL FOOD COST ->",tot_food)
    print("                        TOTAL BEVERAGES COST ->",tot_bev)
    print("                    TOTAL ROOM SERVICE COST ->",tot_room)
    print("                          TOTAL ROOM RENT ->",nights*rooms[customer[name][0]][2])
    print("___________________________________________________________")
    print("                                      “,TOTAL COST=",total_cost)
    print("_________________________________________________________\n")
    print("        _ _ _ _ _ _ _ _ _ _ _ _ _                             _ _ _ _ _ _ _ _ _ _ _ _ _")
    print("            Cashier's Signature                                     Guests Signature")
    print("THANK YOU FOR VISITING OUR PRESTIGEOUS HOTEL. COME AGAING SOON FOR AN AMAZING EXPERIENCE")
    rooms[customer[name][0]][1]='AVAILABLE'


def show_customers():
    os.system('cls')
    L=customer.keys()
    print("\tName\t\tRoom number\tPhone number\t\tAddress\t\t       Check-in\t\t       Check-out")
    for i in L:
        print("  ",i,end="\t        ")
        for j in range(5):
            print (customer[i][j],end="\t                  ")       
        print()
    print("\n")

def search_customer():
    os.system('cls')
    name=input("Enter your name")
    print("Name-",name)
    print("Room number-",customer[name][0])
    print("Phone number-",customer[name][1])
    print("Address-",customer[name][2])
    print("Check-In date and time-",customer[name][3])
    print("Check-out date and time-",customer[name][4])

def review():
    os.system('cls')
    name=input("enter your name")
    review=input("Enter a review of your stay")
    reviews[name]=(review)

def view_reviews():
    os.system('cls')
    Q=reviews.keys()
    for key,value in reviews.items():
        print(f'{key:50}{value}')
                 
def Main():
    while True:
        print("\n\n1-Admin")
        print("2-Customer")
        print("3-Exit program\n\n")

        ch=input("enter your choice-")
        if ch=="":
            print("enter a choice")       
        elif int(ch)==1:
            PASS=input("Enter password for access-")
            if PASS=="S3V3NS3AS":
                print("****************************")
                print("       Access Granted       ")
                print("****************************\n")
                while True:
                    print("\n\n1-input room details")
                    print("2-delete room details")
                    print("3-edit room details")
                    print("4-show room details")
                    print("5-show customer details")
                    print("6-search customer's details")
                    print("7-exit admin options\n")

                    ch=input("enter your choice-")

                    if ch=="":
                        print("Please enter a choice")
                    elif int(ch)==2:
                        delete_room()
                    elif int(ch)==3:
                        edit_room()
                    elif int(ch)==4:
                        show_rooms()
                    elif int(ch)==5:
                        show_customers()
                    elif int(ch)==6:
                        search_customer()
                    elif int(ch)==7:
                        break
                    elif int(ch)==1:
                        input_room()
                    else:
                        print("invalid choice\n")
            else:
                print("INCORRECT PASSWORD\n")

        elif int(ch)==2:
            print("********WELCOME*********\n")
            while True:
                print("1-check available rooms")
                print("2-check in")
                print("3-check out")
                print("4-give review")
                print("5-check reviews of other customers")
                print("6-exit customer options")

                ch=input("Enter your choice")
                if ch=="":
                    print("enter a choice")
                elif int(ch)==1:
                    show_rooms()
                elif int(ch)==2:
                    check_in()
                elif int(ch)==3:
                    check_out()
                elif int(ch)==4:
                    review()
                elif int(ch)==5:
                    view_reviews()
                elif int(ch)==6:
                    break
                else:
                     print("invalid choice")
        elif int(ch)==3:
            while True:
                print("Are you sure you would like to exit the program.")
                print("1-Yes")
                print("2-No")

                ch =input("enter your choice")
                if ch =="":
                    print("enter a choice")
                elif int(ch)==1:
                    exit()
                elif int(ch)==2:
                    break
                else:
                    print("invlid choice")
        else:
            print("invalid choice")
Main()
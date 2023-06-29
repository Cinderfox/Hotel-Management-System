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
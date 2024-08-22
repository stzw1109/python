import userMenu_module

dictOfUser = {}

while True:
    #prints the welcome menu
    userMenu_module.welcome()
    #prompts the user to enter which option they would like to choose in the welcome menu 
    choice = int(input("Enter your choice(e.g 1): "))
    if choice == 1:
        #goes to login page
        userMenu_module.userLogin()
    elif choice == 2:
        #goes to the sign up page
        userMenu_module.userSignUp(dictOfUser)
    elif choice == 3:
        #exits the program
        print("Thank you for coming to the DaBubble Tea Shop")
        exit()
    else:
        #if the user enters an invalid option, the program will ask them to re-enter until a valid option is given 
        print("Invalid choice. Please try again.")

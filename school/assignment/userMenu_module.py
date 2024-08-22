#imports the functionality of the module 
import postLogin_module
import os
import adminSales
import ast

#creates a class for users (parent)
class Users:
    def __init__(self,username,password,age,email):
        self.username = username
        self.password = password
        self.age = age
        self.email = email

    #to show the login status of the user, showing who is currently logged in
    def loginStatus(self):
        print("Current Session: ",self.username)

#creates a class for customers (child)
class Customer(Users):
    #inherits the parents characteristics
    def __init__(self, username, password, age, email):
        super().__init__(username, password, age, email)
    #shows the registered user details
    def customerInfo(self):
        print(f"\nRegistered Info:\n\nUsername: {self.username}\nPassword: {self.password}\nAge: {self.age}\nEmail: {self.email}")

#creates a class for admins (child)
class Admin(Users):
    #inherits the parents characteristics
    def __init__(self, username, password):
        super().__init__(username, password, None, None)

#function for printing the welcome menu
def welcome():
    print("""
    Welcome to DaBubble Tea Shop
    1. Login
    2. Sign Up
    3. Exit
    """)

#appends the signed up  details to the userList.txt file
def listOfUser_File(dictOfUser):
    with open("userList.txt", "a") as userList:
        formatted_string = f"{dictOfUser}"
        userList.write(formatted_string + "\n")

#function for signing up
def userSignUp(dictOfUser):
    print("SIGN UP FORM")
    #prompts the user to enter their details
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    age = int(input("Enter your age: "))
    email = input("Enter your email: ")

    #calling the customer class
    new_customer = Customer(username, password, age, email)
    #storing the details into a dictionary
    userDetails = {'username': username, 'password': password, 'age': age, 'email': email}

    #creates a new file if it doesnt exist
    if not os.path.exists("userList.txt"):
        with open("userList.txt", "w") as userList:
            pass
    
    #reads the file to check whether the user exits or not 
    with open("userList.txt", "r") as userList:
        #iteration used to go through each line in the file
        for lines in userList:
            #removes \n
            lines = lines.strip()

            #if the username already exists, it will prompt the user to try again
            if username in lines:
                print("Username already exists. Please try again.")
                return userSignUp(dictOfUser)
    #passes the details to the listOfUser_File function
    listOfUser_File(userDetails)
    #prints the registered user details
    new_customer.customerInfo()
    print(f"\nUser {username} has been successfully registered.")
    print("\nGoing back to the Main Menu")

#function for login
def userLogin():
    print("LOGIN FORM")
    #if the  user wishes to return to the welcome page, then they can do as instructed
    print("Enter '0' at the username and password to go back to the main menu.\n")
    #prompts the user to enter their details
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")
    #shows the current user logged in
    current_user = Users(username_input, password_input, None, None)

    if username_input == '0':
        print("Going back to the main menu...")
        return
    #admin details
    admin_username = "admin"
    admin_password = "admin123"
    #if admin details are keyed in, then it will direct to the admin page
    if username_input == admin_username and password_input == admin_password:
        print("Admin login successful.")
        current_user.loginStatus()
        adminSales.admin_options()
        return
    #checks if the user exists or not from the userList.txt file
    with open('userList.txt', 'r') as userList:
        readingLines = userList.readlines()
        #if user does not exists then it will redirect to the login page
        if not readingLines:
            print("Invalid username or password or user does not exist. Please try again.\n")
            return userLogin()
        else:
            for line in readingLines:
                #extracts the data from the file as dictionary
                user_info = ast.literal_eval(line)
                #checks if the username and password entered matches the ones in the file
                if user_info['username'] == username_input and user_info['password'] == password_input:
                    #shows the current user logged in
                    current_user.loginStatus()
                    #directs the user to the user's page in the DaBubble Tea Shop
                    return postLogin_module.userOption(username_input)
                    
            #error handling if the username or password are entered correctly, or doesnt exists
            print("Invalid username or password or user does not exist. Please try again.\n")
            return userLogin()




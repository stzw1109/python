import os
import promo
import ast
from datetime import datetime
#initialize the file to be used as sales_file
sales_file = "daily_sales.txt"

#prints the option for admin to choose
def admin_options():
    print("""
        1. View Sales for the Day
        2. Reset Sales Counter
        3. Add New Promo Code
        4. Read User List
        5. Update User Info
        6. Exit Admin Options
    """)
    admin_choice = int(input("Enter your choice(e.g 1): "))
    if admin_choice == 1:
        #calls the function to show the sales for the day
        view_sales()
    elif admin_choice == 2:
        #calls the function to reset the sales
        reset_sales()
    elif admin_choice == 3:
        #calls the function to add new promo code
        promo.addPromo()
        #goes back to the admin page
        admin_options()
    elif admin_choice == 4:
        readUserList()
        return admin_options()
    elif admin_choice == 5:
        update_user_info()
        return admin_options()
    elif admin_choice == 6:
        return
    else:
        print("Invalid choice. Please try again.")
        admin_options()

def update_sales(amount):
    with open(sales_file, "a") as file:
        date_today = datetime.now().strftime("%d/%m/%Y %I:%M%p")
        file.write(f"{date_today} Total Sales: RM{amount:.2f}\n")

#view sales for the day
def view_sales():
    #checks if the sales_file exist or not
    if not os.path.exists(sales_file):
        print("No sales recorded for today.")
        admin_options()
    #reads the file if it exists
    with open(sales_file, "r") as file:
        sales = file.readlines()
    #iterates over each sales, then splits "RM" string to get the sales amount then converting them to float
    total_sales = sum(float(sale.split('RM')[-1]) for sale in sales)
    print(f"Total sales for the day: RM{total_sales:.2f}")
    admin_options()

#resets the sales
def reset_sales():
    #if the sales file exists, then it will proceed to do the next operation 
    if os.path.exists(sales_file):
        #open and read the file
        with open(sales_file, "r") as file:
            previous_sales = file.read()
        #appends the new sale to the file 
        with open("previous_sales.txt", "a") as file:
            file.write(previous_sales + "\n")
        #removes the original sales file,resetting the sales counter
        os.remove(sales_file)
        print("Sales counter reset and previous sales stored.")
    else:
        print("No sales to reset.")
    admin_options()

def update_user_info():
    print("UPDATE USER INFO")

    # Get the username of the user to be updated
    username = input("Enter the username of the user you want to update: ")

    # Read the user list from the file
    with open('userList.txt', 'r') as file:
        lines = file.readlines()

    # Convert each line to a dictionary
    users = [ast.literal_eval(line.strip()) for line in lines]

    # Find the user with the matching username
    user = next((user for user in users if user['username'] == username), None)

    if not user:
        print("User not found. Please try again.")
        return admin_options()

    # Display update options
    print("""
        1. Update Name
        2. Update Password
        3. Update Age
        4. Update Email
        5. Back to Admin Options
    """)
    choice = int(input("Enter your choice: "))

    if choice == 1:
        new_name = input("Enter new name: ")
        # Ensure the new name is different and unique
        while user['username'] == new_name or any(u['username'] == new_name for u in users):
            if user['username'] == new_name:
                print("The new name is the same as the current name. Please enter a different name.")
            else:
                print("Username already exists. Please try again.")
            new_name = input("Enter new name: ")
        user['username'] = new_name
    elif choice == 2:
        new_password = input("Enter new password: ")
        # Ensure the new password is different
        while user['password'] == new_password:
            print("The new password is the same as the current password. Please enter a different password.")
            new_password = input("Enter new password: ")
        user['password'] = new_password
    elif choice == 3:
        new_age = int(input("Enter new age: "))
        # Ensure the new age is different
        while user['age'] == new_age:
            print("The new age is the same as the current age. Please enter a different age.")
            new_age = int(input("Enter new age: "))
        user['age'] = new_age
    elif choice == 4:
        new_email = input("Enter new email: ")
        # Ensure the new email is different
        while user['email'] == new_email:
            print("The new email is the same as the current email. Please enter a different email.")
            new_email = input("Enter new email: ")
        user['email'] = new_email
    elif choice == 5:
        return admin_options()
    else:
        print("Invalid choice. Please try again.")
        return update_user_info()

    # Write the updated user list back to the file
    with open('userList.txt', 'w') as file:
        for u in users:
            file.write(str(u) + '\n')

    print("User info updated successfully.")
    admin_options()

def readUserList():
    # Read the user list from the file
    with open("userList.txt", "r") as file:
        lines = [line for line in file.readlines() if line.strip()]

    # Convert each line to a dictionary and extract necessary information
    users = [
        {key: ast.literal_eval(line.strip())[key] for key in ('username', 'age', 'email')}
        for line in lines
    ]
    # Display each user's information
    print(f"{'Index':<9}{'Username':<15}{'Age':<9}{'Email'}")    
    print("----------------------------------------------------")

    for index, user in enumerate(users, start=1):
    # Print index with fixed width
        print(f"{index:<9}", end="")
        # Define the order of keys for the inner loop to ensure alignment
        keys_order = ['username', 'age', 'email']
        for key in keys_order:
            if key == 'username':
                print(f"{user[key]:<15}", end="")
            elif key == 'age':
                print(f"{user[key]:<9}", end="")
            elif key == 'email':
                print(f"{user[key]}", end="")
        print()  # Move to the next line after printing all details for a user

    # Print the total number of users
    num_users = len(users)
    print(f"\nNumber of users: {num_users}\n")



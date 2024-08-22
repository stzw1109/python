def calculate_price(total_price):
    #globalize the variables from local function to be used in the main function/anywhere in the program
    global order_details,order_deets,price,order_quantity

    #while loop to keep asking the user to enter their order until they type 'done'
    while True:
        order = input("Enter your order and type 'done' to finish.(e.g: M to order Mocha): ").upper()
        if order == 'DONE':
            print("Returning to user page...\n")
            break
        #choices of drinks
        if order == 'A':
            name,drink_price= "Original Pearl Milk Tea",7
            #stores all data returned data from the orderDetails() function
            order_details,order_deets,price,order_quantity,total_price = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        elif order == "B":
            name,drink_price= "Signature Brown Sugar Pearl Milk Tea",7
            order_details,order_deets,price,order_quantity,total_price = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        elif order == "C":
            name,drink_price= "Classic Roasted Milk Tea with Grass Jelly",7
            order_details,order_deets,price,order_quantity,total_price = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        elif order == "D":
            name,drink_price= "Signature Milk Tea",6
            order_details,order_deets,price,order_quantity,total_price = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        elif order == "E":
            name,drink_price= "Passionfruit Green Tea",8
            order_details,order_deets,price,order_quantity,total_price= orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        elif order == "F":
            name,drink_price= "Peach Oolong Tea",8
            order_details,order_deets,price,order_quantity,total_price = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        elif order == "G":
            name,drink_price= "Lychee Black Tea",8
            order_details,order_deets,price,order_quantity,total_price = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        elif order == "H":
            name,drink_price= "Grapefruit Green Tea",8.5
            order_details,order_deets,price,order_quantity,total_price = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        elif order == "I":
            name,drink_price= "Signature Coffee",9
            order_details,order_deets,price,order_quantity,total_price = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        elif order == "J":
            name,drink_price= "Hazelnut Latte",10.2
            order_details,order_deets,price,order_quantity,total_price = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        elif order == "K":
            name,drink_price= "Americano",10
            order_details,order_deets,price,order_quantity,total_price = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        elif order == "L":
            name,drink_price= "Cappucino",10
            order_details,order_deets,price,order_quantity,total_price = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)  
        elif order == "M":
            name,drink_price= "Mocha",11
            order_details,order_deets,price,order_quantity,total_price = orderDetails(name,drink_price,order_details,order_deets,price,order_quantity,total_price)
        else:
            #if user accidentally or pressed wrong input it will continue to prompt user to keep ordering until 'done'
            print("Invalid order. Please choose from the menu.")
            continue
    #prints out the total price ofthe order
    print(f"Your total price is: RM{total_price:.2f}")

    #returns the order details, total price
    return {
        "order_details": order_details, 
        "total_price": total_price
    }





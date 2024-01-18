#Vending Machine

#using function to later call the vending machine along with the items and transactions
#a visual vending machine to imitate how a vending machine looks
def Vending_Machine():
    print('''
 ____________________________________________
|####### Angel's Vending Machine ############|
|#|````````CHOCOLATES`````````|##############|
|#|  =====  ..--''`  |~~``|   |##|````````|##|
|#|  |   |  \     |  :    |   |##| Exact  |##|
|#|  |___|   /___ |  | ___|   |##| Change |##|
|#|  /=__\  ./.__\   |/,__\   |##| Only   |##|
|#|  \__//   \__//    \__//   |##|________|##|
|#|===111=====222======333====|##############|
|#|``````````CHIPS````````````|##############|
|#| =.._      +++     //////  |##############|
|#| \/  \     | |     \    \  |#|`````````|##|
|#|  \___\    |_|     /___ /  |#| _______ |##|
|#|  / __\\\  /|_|\   // __\   |#| |1|2|3| |##|
|#|  \__//-  \|_//   -\__//   |#| |4|5|6| |##|
|#|===444=====555======666====|#| |7|8|9| |##|
|#|``````````DRINKS```````````|#| ``````` |##|
|#| ..--    ______   .--._.   |#|[=======]|##|
|#| \   \   |    |   |    |   |#|  _   _  |##|
|#|  \___\  : ___:   | ___|   |#| ||| ( ) |##|
|#|  / __\  |/ __\   // __\   |#| |||  `  |##|
|#|  \__//   \__//  /_\__//   |#|  ~      |##|
|#|===777=====888======999====|#|_________|##|
|#|```````````````````````````|##############|
|############################################|
|#|||||||| THANK YOU! |||||||||####```````###|
|#||||||||||||PUSH|||||||||||||####\|||||/###|
|############################################|
\\\\\CClvl4\\\\\\\\\\\\\\\\\\\\\\\\\\\///////////////////////
 |_________________________________________|
      ''')

#items to put inside the Vending Machine:
    #Chocolates (3), Chips (3), Drinks (3) = 9 items in total

#dictionary is used to store items along with the codes of the specific item names and their price
    #dictionary name = items, Keys = codes : Values = item name & price
items = {
    111: {"item": "KitKat", "price": 2.75},
    222: {"item": "Snickers", "price": 3.70},
    333: {"item": "M&Ms", "price": 4.35},
    444: {"item": "Lays", "price": 3.50},
    555: {"item": "Pringles", "price": 4.25},
    666: {"item": "Doritos", "price": 3.75},
    777: {"item": "CocaCola", "price": 5.20},
    888: {"item": "Coffee", "price": 6.75},
    999: {"item": "Water", "price": 2.00}
}

#function to display the items of the vending machine to the user
def display_items():
    print("Vending Machine Items:")
    #for loop, assigns the item_code and item_info in the dictionary "items" per item in the machine
    for item_code, item_info in items.items():
        #f-string for iputing the specific items and their prices in the display
        #that would follow the format: "item code. item - price" 
            #with a two decimal (.2f) price formatting for the money needed
        print(f"\t{item_code}. {item_info['item']} - AED {item_info['price']:.2f}")

#function for the user input of purchasing 
        #and process the transaction of purchasing and exchanging money
def vending_item():
    #inserting the previous functions of "Vending_Machine" and "Display_Items" 
        #to included with the output/printing of the purchasing and transaction
    Vending_Machine()
    display_items()
    #while loop in true, to have a continous purchasing of items for the user
    while True:
        #try block is used for attempt and condition making in this vending machine, 
            #to have an alternative response to the errors that are made from the user's end
        try:
            #a variable called "user_choice" to name the integer/number input of the user 
            user_choice = int(input("\nEnter the code for the item you want to purchase or 0 to exit: "))
            #if statement, for the user to break the while loop
            #since the user is required to input an integer data type, the condition variable would also be an integer "0"
            if user_choice == 0:
                #when the variable "0" is identified, the loop will first print a message for the user
                print("Thank you for using Angel's Vending Machine!")
                #the if condition will then process the break of the loop, stoping the vending machine
                break
            #else-if statement, for when the user inputs the code, purchases an item, and the money transaction 
            #variable "user_choice" identifies the item_code and item_info in the dictionary "items"
            elif user_choice in items:
                #a new variable used for the money transaction called "user_money" to name the amount of the user's input
                #float data type for the decimal placing of the amount the user will input to pay
                #f-string to place the specific item the user has chosen
                user_money = float(input(f"\tEnter the amount of money you want to spend on {items[user_choice]['item']}: "))
                #if statement, when the user_money is equal to the price of the item chosen
                if user_money >= items[user_choice]['price']:
                    #new variable "change" with the equation (-) subtraction is used for the change of the user
                    change = user_money - items[user_choice]['price']
                    #print statement of dispensing the item the user has chosen and paid
                    print(f"\n...Dispensing {items[user_choice]['item']}...\n")
                    #another if statement, for when the user_money is greater than the price of the item chosen and has a change for the paid amount
                    if change > 0:
                        #a print statement returning the change of the user
                        #f-string to place the variable "change" with a two decimal (.2f) and the item the user has chosen
                        print(f"\tReturning change of AED {change:.2f} for {items[user_choice]['item']}...\n")
                #else statement, when a user has input an amount less than the price of the item chosen
                else:
                    #print statement to let the user know the item chosen and its amount needed
                    #f-sting for the item chosen and the price with a two decimal (.2f)
                    print(f"Insufficient money to purchase {items[user_choice]['item']}. Please insert at least AED {items[user_choice]['price']:.2f}.")
            #else statement, when the user inputs the incorrect item code
            else:
                print("Invalid selection. Please try again.")
        #except block name "ValueError", in cases when a user inputs a different data type from the required integer data type 
        except ValueError:
            print("Invalid input. Please enter a number.")

#calling the vending_item function to start the Vending Machine
    #calling this funciton would also have the previous functions of "Vending_Machine" and "Display_Items" running
vending_item()
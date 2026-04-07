#push test

product_list = ["coffee", "Tea", "Sugar", "milk", "green tea"]

def main_menu(): #WORKING
   
    while True:
        try:
             print()
             print("*****      MAIN MENU        *****")
             print()
             print("*****   0 - Exit            *****")
             print("*****   1 - Prduct Menu     *****")
             print()
             choice = int(input("Select an option: "))
             print()
             if choice == 0:
                exit()
             elif choice == 1:
                product_menu()
        except ValueError:
            print("** INVALID INPUT ** Please use either 1 or 0")

def product_menu():#WORKING
    while True:
        print()
        print("*****   0 - Return to Main Menu   *****")
        print("*****   1 - Print Product List    *****") #print list
        print("*****   2 - Create New Product    *****") #create new and append
        print("*****   3 - Update Product        *****") #update product | print list with index > get user input for product index > get user input for new name > upadate            
        print("*****   4 - Remove Product        *****") #delete product | print with index > delete by index value
        print()

        try:
            choice = int(input(f'Please choose an item from the list: '))
            if choice == 0:
                return
            elif choice == 1:
                print_list()
            elif choice == 2:
                add_product()
            elif choice == 3:
                update_product()
            elif choice == 4:
                remove_product()
        except ValueError:
            print("** Invalid Input **")
       
def add_product():#WORKING
    while True:

        print("#ADD PRODUCT") #debug        
        product = (str(input(f'Please add a new product: ')))
    
        try:
            choice = (int(input(f'Are you sure you want to add {product}? (1) Yes (2) No >')))
            if choice == 1:
                product_list.append(product)
                print()
                print(f'{product} has been added to the list')
            else:
                print("** Action Cancelled **")

            choice2 = int(input("Would you like to add another item? (1) Yes (2) No > "))
            if choice2 != 1:
                break

        except ValueError:
            print("** INVALID INPUT ** Please enter a number (1 or 2).")
          
def update_product():#WORKING
    while True:

        print_list()
        try:
            update_index = int(input(f'Please enter the index number of the item you want to update: '))
            
            old = product_list[update_index]
            
            print()
            print(f'The current item at index {update_index} is {old}')

            new = str(input("Enter the new name for the product: "))
            product_list[update_index] = new
            print()

            print(f'* Update Complete * {old} has now been updated to {new}')
            print()
            choice = int(input("Would you like to update another item? (1) Yes (2) No > "))
            if choice == 1:
                break
            elif choice == 2:
                return
        except ValueError:
            print(" ** Invalid Input ** Please enter a valid number")

def remove_product():#WORKING
    
    remove_index = (int(input(f'Please choose item (by index number) to remove: ')))

    deleted_item = product_list[remove_index]

    choice = (int(input(f'Are you sure you want to remove {product_list[remove_index]}? (1) Yes (2) No > ')))
    
    if choice == 1:
        product_list.pop(remove_index)
        print(f'{deleted_item} has been removed to the list')

    elif choice == 2:
        return

def print_list():#WORKING
     
     j = 0
     
     print("#PRINT LIST")
     print()
     for i in product_list:
        print(j, " ", i, sep="")
        j+=1
     print()
    

    
main_menu()








 #create new and append
 #update product | print list with index > get user input for product index > get user input for new name > upadate
 #delete product | print with index > delete by index value








    
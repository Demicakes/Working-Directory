productlist = ["Coffee", "Tea", "Sugar", "Milk"] #list populated for debug but will be cleared 

def main_menu(): # 1 FOR PRODUCT MENU 0 TO EXIT

    x = 5 
    y = 10
    print(x,y)

    print()
    print("--------------------------------------------")
    print() 
    print("    *****   Welcome to the Main Menu   *****")
    print()
    print("--------------------------------------------")
    print()
    print("             Press 0 to exit                ")
    print("             Press 1 for products menu      ")
   
    choice = int(input(""))

    if choice ==1:
        product_menu()
    elif choice == 0:
        exit()

def print_list():# LIST TO BE PRINTED VERTICALLY WITH INDEX NUMBER 
     print("#PRINT LIST") #DEBUG

     j = 0
     print()
     
     for i in productlist:
        print(j, " ", i, sep="")
        j+=1
     print()
    
def product_menu(): #SELECT A RANGE OF OPTIONS 1. PRINT PRODUCT LIST 2. ADD PRODUCT 3.UPDATE PRODUCT 4.REMOVE PRODUCT. AND 0 TO RETURN TO MAIN MENU
      print("PRODUCT MENU") #DEBUG

      print_list()
      
def add_product(): # ADD NEW PRODUCTS TO A LIST
        newproduct = str(input(f'Please add a new product: '))
        productlist.append(newproduct)
        print(productlist)
        
def remove_product():# REMOVE PRODUCTS FROM A LIST USING INDEX NUMBER
    print("#REMOVE PRODUCT") #DEBUG

    remove_index = int(input(f'Please select item (by index) to remove: '))
    deleted_item = productlist[remove_index]

    print()
    choice = int(input((f'Are you sure that you want to delete {productlist[remove_index]}? ')))
    if choice == 1:
        productlist.pop(remove_index)
        print(f'ITEM REMOVED - {deleted_item} has been removed from the product list')

    elif choice == 0:
        return()

def update_product(): # UPDATE PRODUCT USING INDEX
    print()

def countdown():
     
    counter = 10

    while counter != 0:
            print(f'T-minus {counter}')
            time.sleep(1)
            counter -= 1
    print('Blast off!!!')





productlist = ["Coffee", "tea", "sugar", "milk"] 




def do_loop():


    #for loop

    j=0                                 # j is used as a place holder to add +1 every loop

    for i in productlist:               # create the for loop and create a variable called i    
        print(j, i, sep =" ")           # the loop will run for each item in productlist
        j+=1                            # this adds + 1 to j every itteration



def main_menu(): # 1 FOR PRODUCT MENU 0 TO EXIT

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

def product_menu(): #SELECT A RANGE OF OPTIONS 1. PRINT PRODUCT LIST 2. ADD PRODUCT 3.UPDATE PRODUCT 4.REMOVE PRODUCT. AND 0 TO RETURN TO MAIN MENU
      print("this is a product menu")

def add_product(): # ADD NEW PRODUCTS TO A LIST


    newproduct = str(input(f'Please add a new product: '))

    productlist.append(newproduct)

    print(productlist)

def remove_product():# REMOVE PRODUCTS FROM A LIST USING INDEX NUMBER


    print("this is where you remove a product")

def update_product(): # UPDATE PRODUCT USING INDEX
    print()

main_menu()



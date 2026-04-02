#int variables 
numX = 5
numY = 10

print ("numX = 5") #simple print of string
print ("numY =", + numY) #print string with a int variable 

#using def to create functions for use later rather than retyping the same code

#addion
def Addition():
    print()
    print ("Addition")
    print("numX + numY")
    print (numX + numY)

#subtraction
def Subtraction():
    print()
    print("Subtraction")
    print("numX - numY")
    print (numX - numY)

#division
def Division():
    print()
    print("Division")
    print("numY / numX")
    print (numX / numY)

#multiply
def Multiply():
    print()
    print("Multiply")
    print("numX * numY")
    print (numX * numY)
    print()

#boolean
def bool_function():
    print("Boolean")
    print ("does nunX = numY")
    print ("Result = ", numX == numY)
    print()

#IF statement with gretaer or equal to 
def if_statements():
    if numY >= numX:
        print ("If numX is greater or equal to numY, print true")
        print ("True")
        print()

    else: #else if can also be used as elif 
        (print ("False"))
        print()

#making a list
leeds_squad = ["Daniel Farke", "Lucas Perri", "Jayden Bogle", "Gabriel Gudmundsson", "Ethan Ampadu",
               "Pascal Struijk", "Joe Rodon", "Daniel James", "Sean Longstaff", "Dominic Clavert-Lewin", "Joël Prioe", "Brenden Aaronson"]

#print horizontal
print (*leeds_squad, sep=", ")
print()

def loop_function():
    #print vertical with shirt numbers
    i = 0 #variables only apply to the function and not outside
    j = 0

    for i in leeds_squad:
        print(j, " ", i, sep="")
        j+=1
    print()

#add nationalities to players
nation = ["Germany", "Brazil", "England", "Sweden", "Wales", "Netherlands", "Wales", "Wales", 
          "England", "England", "Netherlands", "USA"]

#adding nations to list via zip and enumerate - this is new for me but i understand it
def loop_w_nations():
    for j, (player, country) in enumerate(zip(leeds_squad, nation)):
        print(f'{j} {player} ({country})')
        

def loopy_w_nations():
    for j, (player, country) in enumerate(zip(leeds_squad, nation)):
        print(f'{j} {player} - {country}')







#bringing it all together, calling each function (doesnt have to be in any order)
Addition()
Subtraction()
Division()
Multiply()
bool_function()
if_statements()
loop_function()
loop_w_nations()


print()











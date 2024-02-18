from pyfiglet import Figlet
f = Figlet(font = "slant")
print(f.renderText("Dan Dan Store ~"))

def menu():
    print(" ")
    print("1. Add Product.")
    print("2. Edit Product.")
    print("3. Delete Product.")
    print("4. Search.")
    print("5. Show All.")
    print("6. Buy.")
    print("7. Exit.")

product = []

def load():
    print("Loading...")
    p = open("my store\database.txt", "r")
    producttext = p.read()
    row = producttext.split("\n")

    for i in range(len(row)):
        info = row[i].split(",")
        product.append({"id":info[0], "name":info[1],
                        "price":info[2], "number":info[3]})
    print(" ")
    print("Welcome!")

def Add():
    id = int(input("Enter the id of new product: "))
    name = input("Enter the name of new product: ")
    price = int(input("Enter the price of new product: "))
    number = int(input("Enter the number of new product: "))
    product.append({"id":id, "name":name, "price":price, "number":number})

def ShowEditList():
    print("1. Name:")
    print("2. Price:")
    print("3. Number:")
    print("4. Exit.")

def Edit():
    id = int(input("Enter the id of product: "))
    for i in range(len(product)):
        if product[i]["id"]== id:
          while True:
            ShowEditList()
            choose = int(input("Enter a number from list: "))
            if choose == 1:
                product[i]["name"] = input("Rename the product -> ")

            elif choose ==2:
                product[i]["price"]=float(input("Reprice the product -> "))

            elif choose == 3:
                product[i]["number"]=int(input("Enter the number the product -> ")) 

            elif choose == 4:
                break

            else:
                print("Invalid number.")

def DeleteProduct():
    id = int(input("Enter the product id -> "))
    for i in range(len(product)):
        if product[i]["id"] == id:
            del product[i]
            print("Product removed!")
            break
        else:
            print("This id doesn't exist!")

def Search():
    UserSearch= input("Enter the name of your product -> ")
    for i in range(len(product)):
        if product[i]["name"] == UserSearch:
            print(product[i])
        else:
            print("Product didn't found!") 

def Show():
    for i in range(len(product)):
        print(product[i]["id"], "\t", product[i]["id"], "\t",
              product[i]["id"], "\t", product[i]["id"], "\t")

#def Buy():

def ExitStore():
    print("Thanks for comming!")
    exit()

load()
menu()

print("")
choice = int(input("Choose a number: "))

if choice==1:
    Add()
elif choice==2:
    Edit()
elif choice==3:
    DeleteProduct()
elif choice==4:
    Search()
elif choice==5:
    Show()
elif choice==6:
    pass
elif choice==7:
    ExitStore()
"""
Program: warehouse control
Author: Ingrid
Functionality: 
    - Register Items
        - id (auto generated): int
        - title: str
        - category: str
        - stock: int
        - price: float

"""

# imports
from menu import print_menu, clear, print_item, print_header
from item import Item 
import pickle


# global vars
catalog = []
last_id = 0
data_file = 'warehouse.data'
temp_prices =[]

# functions

def serialize_catalog():
    global data_file
    writer = open(data_file, 'wb') #wb => create/overwrite the file
    pickle.dump(catalog, writer)
    writer.close()
    print(' Data saved! ')

def deserialize_catalog():
    global data_file
    global last_id
    try:
        reader = open(data_file, 'rb') #rb => read binary, throw exception if file does not exist
        temp_list = pickle.load(reader)

        for item in temp_list:
            catalog.append(item)

        last = catalog[ -1 ]
        last_id = last.id +1
        how_many = len(catalog)
        print(' Deserialized ' + str(how_many) + ' items ')
    except: 
        print("Error, ")



def register_item():
    global last_id
    try: 
        print_header("Register new Item")
        title = input('Please provide the title: ')
        category = input('Please provide category: ')
        stock = int(input('Please provide stock: '))
        price = float(input('Please provide price: '))

        the_item = Item(last_id, title, category, stock, price)
        last_id += 1
        catalog.append(the_item)
        
        count = len(catalog)
        print(" Item saved, you have " + str(count) + " items in your catalog ")

    except ValueError:
         print("Error, provide valid numbers")
    except:
         print("Error, please verfiy data")

def display_catalog():
    #input('test')
    #print_header("Your catalog")
    for item in catalog:
        print_item(item)

def out_of_stock():
    print_header("Items out of stock")
    for item in catalog:
        if(item.stock == 0):
            print_item(item)

def total_stock_value():
    print_header("total stock value")
    total = 0.0
    for item in catalog:
        total += item.stock * item.price
    
    print('The total is: $ ' + str(total))

def update_price():
    display_catalog()
    id = input ('Please choose an id: ')
    found = False
    for item in catalog:
        if(str(item.id) == id):
            found = True
            price = float(input("Provide new price $"))
            item.price = price

    if(not found):
        print("Error, invalid ID, try again")

def delete_item():
    display_catalog()
    id = input ('Please choose an item ID to remove : ')
    found = False
    for item in catalog:
        if(str(item.id)== id):
             found = True
             catalog.remove(item)
             print('Item has been deleted')
        if (not found):
            print(" ERORR, invalid ID, not found.")

def update_stock_value():
    display_catalog()
    id = input ('Please choose an id:')
    found = False
    for item in catalog:
        if(str(item.id) == id):
            found = True
            stock_value = float(input("Provide new stock value: "))
            item.stock = stock_value

    if(not found):
        print("Error, invalid ID, try again")

def display_categories():
    print_header("Unique categories")
    temp = []
    for item in catalog:
        if(not item.category in temp):
            temp.append(item.category)
            print(item.category)

def cheapest_product():
    print_header("Cheapest Product")
    cheapest = catalog[0] # first on the list
    for item in catalog: # travel array and compare 
        if(item.price < cheapest.price):
            cheapest = item   # keep item as the cheapest
    print_item(cheapest)

def sorted_top_prices():
    
    #temp_prices = []  MOVED TO GLOBAL VAR
    for item in catalog:
        temp_prices.append(item.price) #array with only prices
    
    temp_prices.sort(reverse=True) # sorted prices from large to small

    #slice top 3 to only show first 3 prices in list
    # print(temp_prices[0:3])

def most_expensive():
    print_header("3 Most Expensive Products")
    for item in catalog:
        if(item.price == temp_prices[0]):
            print_item(item)
   
    for item in catalog:
        if(item.price == temp_prices[1]):
            print_item(item)
    
    for item in catalog:
        if(item.price == temp_prices[2]):
            print_item(item)
    
    
    

# instructions
deserialize_catalog()
input ('Press Enter to continue...') #putting input bc otherwise it'll go to 'clear'

opc = ''
while(opc != 'x'):
    clear()
    print_menu()
    opc = input('Please select an option: ')
    print(opc)

    if ( opc == '1'):
        register_item()
        serialize_catalog()

    elif(opc == '2'):
        # create a function, call, travel the list and display the title.title
        display_catalog()
    
    elif(opc == '3'):
        out_of_stock()
        # call the fn
        # create the fn
        # travel the list
        # if item.stock is equal to zero
        # display_item
    elif(opc == '4'):
        total_stock_value()

    elif(opc == '5'):
        update_price()
        serialize_catalog() # everytime we modify the data, we are saving the changes

    elif(opc== '6'):
        delete_item()
        serialize_catalog()

    elif(opc == '7'):
        update_stock_value()
        serialize_catalog()

    elif(opc == '8'):
        display_categories()
    
    elif(opc == '9'):
        cheapest_product()
    
    elif(opc == '10'):
        sorted_top_prices()
        most_expensive()
        

    input('Press Enter to continue...') 

#Recommendations for updating price
"""
- show catalog 
- ask the user to choose an id
- find the id in the catalog
    ask for the new price
    set the price
- else, show an error
"""
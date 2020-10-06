
import os

# functions

def print_menu():
    print(" - " * 30)
    print ( " Warehouse control ")
    print(" - " * 30)

    print('[1] Register new Item')
    print('[2] Display catalog')
    print('[3] Display items out of stock')
    print('[4] Display stock value') 
    print('[5] Update item price') 
    print('[6] Delete item') #HW
    print('[x] Close')

def clear():
    command = 'clear'
    if(os.name == 'nt'):
        command = 'cls'
    return os.system(command)

def print_item(item):
    print(str(item.id)
     + " | " + item.title 
     + " | " + item.category.rjust(5)
     + " | " + str(item.stock) 
     + " | " + str(item.price) 
     )

     # rjust(#)

def print_header(title):
    clear()
    print("-" * 50)
    print(title)
    print("-" * 50)


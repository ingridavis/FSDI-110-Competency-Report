
import os
import datetime

# functions

def print_menu():
    print(" - " * 17)
    print ( " Warehouse control    " + get_datetime())
    print(" - " * 17)

    print('[1] Register new Item')
    print('[2] Display catalog')
    print('[3] Display items out of stock')
    print('[4] Display stock value') 
    print('[5] Update item price') 
    print('[6] Delete item') #HW
    print('[7] Update stock value')
    print('[8] Display categories')
    print('[x] Close')

def get_datetime():
    now = datetime.datetime.now()
    return now.strftime('%b/%d/%Y/%T')

def clear():
    command = 'clear'
    if(os.name == 'nt'):
        command = 'cls'
    return os.system(command)

def print_item(item):
    print(str(item.id)
     + " | " + item.title.ljust(20)
     + " | " + item.category.ljust(12)
     + " | " + str(item.stock).rjust(5)
     + " | $" + str(item.price).rjust(10)
     )

     # rjust(#)

def print_header(title):
    clear()
    print("-" * 50)
    print(title)
    print("-" * 50)


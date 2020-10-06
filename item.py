
class Item:
    id = 0
    title = ''
    category = ''
    stock = 0
    price = 0.0

# new constructor 

    def __init__(self, id, title, cat, stock, price):
    # receive self first, don't have to use same name, but it's recommended
    # assigning new variable
        self.id = id
        self.title = title
        self.category = cat
        self.stock = stock
        self.price = price




# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus):
    valid_items = {"A","B","C","D"}
    prices = {"A":50, "B": 30, "C": 20, "D": 15}

    offers = {"A": (3,130), "B": (2,45)} #stores special offers (offer quantity, offer price)

    #loop responsible for validating the input
    for x in skus: 
        if x not in valid_items:
            return -1
        

    counter = {item: skus.count(item) for item in valid_items}

    total = 0

    #loops through each item, gets quantity, checks if item has a special offer, and if so it calculates total price by combining offer prices and remaining item prices
    
    for item in valid_items:
        quantity = counter[item]
        if item in offers:
            offer_quantity, offer_price = offers[item]
            total += (quantity // offer_quantity) * offer_price
            total += (quantity % offer_quantity) * prices[item]
        else:
            total += quantity * prices[item]

    return total
        
    

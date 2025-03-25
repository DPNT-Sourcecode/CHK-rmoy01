

# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus):
    valid_items = {"A","B","C","D", "E"}
    prices = {"A":50, "B": 30, "C": 20, "D": 15, "E": 40}

    #stores special offers (offer quantity, offer price)

    offers = {
        "A": [(5,200),(3,130)], 
        "B": [(2,45)]
    } 

    #initialises free offer with required quantity and free item alongside each other
    free_offers = {
        "E": (2,"B")
    }

    #loop responsible for validating the input
    for x in skus: 
        if x not in valid_items:
            return -1
        

    counter = {item: skus.count(item) for item in valid_items}

    for item, (req_quantity, free_item) in free_offers.items():
        free_units = counter[item] // req_quantity
        if free_item in counter:
            counter[free_item] = max(0, counter[free_item] - free_units)

    total = 0

    #loops through each item, applies any offers and calculates the total

    for item in valid_items:
        quantity = counter[item]
        if item in offers:
            for offer_quantity, offer_price in offers[item]:
                offer_applied = quantity // offer_quantity
                total += offer_applied * offer_price
                quantity %= offer_quantity
        
        total += quantity * prices[item]

    return total
        
    

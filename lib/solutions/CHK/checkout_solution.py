

# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus):
    valid_items = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    prices = {
        "A":50, "B": 30, "C": 20, "D": 15, "E": 40,
        "F": 10, "G": 20, "H": 10, "I": 35, "J": 60,
        "K": 70, "L": 90, "M": 15, "N": 40, "O": 10,
        "P": 50, "Q": 30, "R": 50, "S": 20, "T": 20,
        "U": 40, "V": 50, "W": 20, "X": 17, "Y": 20,
        "Z": 21
    }

    #stores special offers (offer quantity, offer price)

    offers = {
        "A": [(5,200),(3,130)], 
        "B": [(2,45)],
        "H": [(10,80), (5,45)],
        "K": [(2,120)],
        "P": [(5,200)],
        "Q": [(3,80)],
        "V": [(3,130), (2,90)]
    } 

    #initialises free offer with required quantity and free item alongside each other
    free_offers = {
        "E": (2,"B"),
        "N": (3,"M"),
        "R": (3,"Q"),
    }
    
    #self-reducing offers
    self_free_offers = {
        "F":(3,),
        "U":(4,)
    }

    group_discount_items = ["S","T","X","Y","Z"] #3 for 45 rule

    #loop responsible for validating the input
    for x in skus: 
        if x not in valid_items:
            return -1
        

    counter = {item: skus.count(item) for item in valid_items}

    for item, (req_quantity, free_item) in free_offers.items():
        free_units = counter[item] // req_quantity
        if free_item in counter:
            counter[free_item] = max(0, counter[free_item] - free_units)

    #loop applies self reducing offers
    for item, (group_size,) in self_free_offers.items():
        total_count = counter[item]
        free_units = total_count // group_size
        counter[item] = total_count - free_units

    total = 0

    #loop handles group discount
    group_items = []
    for item in group_discount_items:
        group_items += [item] * counter[item]
        counter[item] = 0
    
    group_items.sort(key=lambda i: prices[i], reverse=True) #prioritise expensive items
    while len(group_items)>= 3:
        total+= 45
        group_items = group_items[3:]
    
    for item in group_items:
        total+= prices[item]

    #loops through each item, applies any offers & calculates the total

    for item in valid_items:
        quantity = counter[item]
        if item in offers:
            for offer_quantity, offer_price in offers[item]:
                offer_applied = quantity // offer_quantity
                total += offer_applied * offer_price
                quantity %= offer_quantity
        
        total += quantity * prices[item]

    return total
        
    


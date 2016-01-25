__author__ = 'Avi'

def increase_it(quantity):
    return quantity * 1.5

butter = .75
baking_soda = 1.5
flour = 2
salt = .5
bananas = 4
sugar = 1
eggs = 2
vanilla = 1

ingrediants = [butter,baking_soda,flour,salt,bananas,sugar,eggs,vanilla ]

for item in ingrediants:
    print(increase_it(item))
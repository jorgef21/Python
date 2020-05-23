"""
For a given pair of Array flavors['Vanilla','Chocolate'] and toppings['Caramel','Chocolate chips']

Find the posible combinations between flavors and toppings
example:

[['Vanilla','Caramen'],['Vanilla','Chocolate Chips'],['Chocolate','Caramel'],['Chocolate','Chocolate Chips']]
"""
from itertools import combinations

def comb(flavors,toppings): 
   return [[f,t] for f in flavors for t in toppings]

def main():
    print(comb(['Vanilla','Chocolate'],['Caramel','Chocolate Chips','Oreo']))

if __name__=='__main__':
    main()
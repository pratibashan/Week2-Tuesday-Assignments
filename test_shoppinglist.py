
import unittest
from shoppinglist import ShoppingList
from shoppinglist import GroceryItem

class TestShoppingList(unittest.TestCase):
    
    def setUp(self):
         print("SETUP")
         #self.sl = ShoppingList()
         

    def test_create_view_shoppingList(self):

        print("test_create_view_shoppingList")

        self.walmart_sl = ShoppingList('Walmart','')
        self.costco_sl = ShoppingList('Costco','')
        self.fiesta_sl = ShoppingList('Fiesta','')
        self.sprouts_sl = ShoppingList('Sprouts','')

        
        #self.sl.set_storenames('Walmart','')

        self.walmart_sl.add_groceryitem(GroceryItem('Milk',2,1)) 
        self.walmart_sl.add_groceryitem(GroceryItem('Egg',2,10)) 
        self.walmart_sl.add_groceryitem(GroceryItem('Nuts',2,2)) 
        self.walmart_sl.add_groceryitem(GroceryItem('Chicken',2,1)) 


        self.costco_sl.add_groceryitem(GroceryItem('Paper',2,1)) 
        self.costco_sl.add_groceryitem(GroceryItem('Plates',2,10)) 
        self.costco_sl.add_groceryitem(GroceryItem('Napkins',2,2)) 
        self.costco_sl.add_groceryitem(GroceryItem('Chips',2,1)) 

        self.fiesta_sl.add_groceryitem(GroceryItem('Milk',2,1)) 
        self.fiesta_sl.add_groceryitem(GroceryItem('Juice',2,10)) 
        self.fiesta_sl.add_groceryitem(GroceryItem('Potato',2,2)) 
        self.fiesta_sl.add_groceryitem(GroceryItem('Mango',2,1)) 

        self.sprouts_sl.add_groceryitem(GroceryItem('Sugar',2,1)) 
        self.sprouts_sl.add_groceryitem(GroceryItem('Salt',2,10)) 
        self.sprouts_sl.add_groceryitem(GroceryItem('Chicken',2,2)) 
        self.sprouts_sl.add_groceryitem(GroceryItem('Fish',2,1)) 

    
        print("=================================")
        self.walmart_sl.view_groceryitem()
        print("=================================")
        self.costco_sl.view_groceryitem()
        print("=================================")
        self.fiesta_sl.view_groceryitem()
        print("=================================")
        self.sprouts_sl.view_groceryitem()

        self.fiesta_sl.get_itemprice('Juice')
        

        print("=================================")
        self.walmart_sl.remove_groceryitem('Milk')
        self.walmart_sl.remove_groceryitem('Chicken')

        self.walmart_sl.view_groceryitem()



    def tearDown(self):
        print("TEAR DOWN")


if __name__ == ' __main__ ':
    unittest.main()
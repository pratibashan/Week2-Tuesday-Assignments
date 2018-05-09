

class GroceryItem:
    def __init__(self,item,price,quantity):
        self.item = item
        self.price = price
        self.quantity = quantity

class ShoppingList:

    def __init__(self,title,description):
        self.title = title
        self.description = description
        self.groceryitems = []
        self.storenames =[]


    # def set_storenames(self,title,description):
    #     print(f"{title[0]}")
    #     # for index in range(len(title)):
    #     #     if (title[index] !=:
    #     #         self.storenames.append(name)
    #     #     else:
    #     #         print("Shopping list name already exists!")

    def add_groceryitem(self,gi):  
        self.groceryitems.append(gi) 
       
        
    def view_groceryitem(self):
        print(f"{self.title} :")
        print("-----------------")
        for grocerylist in self.groceryitems:
                print(f"{grocerylist.item}") 

          
    
    def remove_groceryitem(self,gi_item):
        for index in range(0,len(self.groceryitems)):
            if (self.groceryitems[index].item == gi_item):
                self.groceryitems.remove(self.groceryitems[index])
                break

    def get_itemprice(self,gi_item):
        for index in range(0,len(self.groceryitems)):
            if(self.groceryitems[index].item == gi_item):
                print("================================")
                print(f"The {gi_item} price is {self.groceryitems[index].price}")


                
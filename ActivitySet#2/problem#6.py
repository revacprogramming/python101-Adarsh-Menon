class Menu:

    def __init__(self,add_menu,price_menu):
        self.add_menu=add_menu
        self.price_menu=price_menu

    def add(self):
        print("the menu is ",self.add_menu,"price is",self.price_menu)
    

m1=Menu("idily",10)
m2=Menu("Vada",20)
m1.add()
m2.add()


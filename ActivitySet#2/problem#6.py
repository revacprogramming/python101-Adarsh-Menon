

class Menu:
    """fill in class definition here"""
  def __init__(self,add_menu,price_menu):
      self.add_menu=add_menu
      self.price_menu=price_menu

  def add(add_menu,price_menu):
      print("the menu is ",add_menu,"price is",price_menu)
    


m = Menu()  # Menu is a class
m.add("idly", 10)
m.add("vada". 20)

m.show()


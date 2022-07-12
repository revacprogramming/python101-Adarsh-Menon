

class Menu:
    """fill in class definition here"""


m = Menu()
m = m + ("idly", 10) + ("vada", 20)  
# Hint: operator overloading special methods? (__add__, __sub__, etc.)

print(m)  # should print the menu properly
def __init__(self,add_menu,price_menu):
      self.add_menu=add_menu
      self.price_menu=price_menu

  def add(add_menu,price_menu):
      print("the menu is ",add_menu,"price is",price_menu)
    


m = Menu()  # Menu is a class
m.add("idly", 10)
m.add("vada". 20)

m.show()
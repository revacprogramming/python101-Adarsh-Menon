def get_cs():
  s=str(input("enter the str"))
  return s


def cs_to_lot(l):
  j=[]
  m=l.split(";")
  for i in m:
    n=i.split("=")
    s=tuple(n)
    j.append(s)
  return j
  print(j)
    
    
def lot_to_cs(lot):
  """convert list of strings to connected string"""
  print(lot)
  for i in lot:
    s=""+i[0]+"="+i[1]
    print(s,end=";")
    
    
def main():
    l = get_cs()
    lot = cs_to_lot(l)
    cs=lot_to_cs(lot)


if __name__ == '__main__':
    main()

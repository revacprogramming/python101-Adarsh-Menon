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
  print(j)
    
    


def main():
    l = get_cs()

    lot = cs_to_lot(l)



if __name__ == '__main__':
    main()

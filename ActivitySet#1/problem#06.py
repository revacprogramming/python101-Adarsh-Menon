# Loops & Iterators

def largest():
  largest=0
  l=[]
  total=int(input("enter how many element you need"))
  for i in range(0,total):
    m=int(input("enter int"))
    l.append(m)
  for j in l:
    if j>largest:
       largest=j
  print(largest)
    

largest()

def smallest():
  l=[]
  total=int(input("enter how many element you need"))
  for i in range(0,total):
    m=int(input("enter int"))
    l.append(m)
  smallest=min(l)
  print(smallest)

samllest()
    



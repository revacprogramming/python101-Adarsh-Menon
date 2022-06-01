# Lists

def fuc():
  filename = open("dataset/romeo.txt")
  lst=list(filename)
  l=[]
  for word in lst:
    for letter in word:
      if letter != l:
        l.append(letter)
        l.sort()
        
  print(l)
        

def inputt():
    a=int(input("enter number"))
    return a
    
    
def add(a,b):
    n=a+b
    return n
    
def out(a,b,n):
    print("sum of",a,"+",b,"=",n)
    
def main():
    a=inputt()
    b=inputt()
    n=add(a,b)
    out(a,b,n)
    
main()
fuc()

# Regular Expressions
# https://www.py4e.com/lessons/regex

def file():
  file=open("dataset/regex.txt")
  sum=0
  m=[]
  for l in file:
    for n in l:
      m.append(n)
      for j in m:
       if j.isdigit==True:
         sum=sum+int(j)
         print(j)
         print(sum)
         
         

file()

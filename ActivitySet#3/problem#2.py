def con_fraction():
    n=eval(input("enter the no of digits"))
    s=list(n)
    n=""
    summ=0
    if len(s)>1:
        for i in s:
            summ=summ+1/i
            print("1/",i,"+",n)
        print("=",summ)
con_fraction()
    
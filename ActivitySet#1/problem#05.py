# Functions


def computepay(h, r):
    result=0
    if h<=40:
	   result = h*r
    else:
       o = h-40
       result = o*(r*1.50) + 40*r
    return result

p = computepay(45,10.5)
print("Pay", p)

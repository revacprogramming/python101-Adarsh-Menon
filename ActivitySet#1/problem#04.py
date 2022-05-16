# Conditional Execution



def pay(hrs,rph):
  h = float(hrs)
  r = float(rph)
  result=0
  if h<=40:
	  result = h*r
  else:
    o = h-40
    result = o*(r*1.50) + 40*r
  return result

pay(10.5,1.5)

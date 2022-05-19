def cs_to_lot(cs):
  """convert connected string to list of strings"""
  n=[]
  for i in cs:
    n.append((i,i[0]))
  return n


def lot_to_cs(lot):
  """convert list of strings to connected string"""
  for i in lot:
    print(i[0],"=",i[1])
  


def main():
    cs=get_cs()

    lot=cs_to_lot(cs)  # convert connect string to list of tuples
    print(lot)

    cs=lot_to_cs(lot)  # convert list of strings to connect string


if __name__ == '__main__':
    main()

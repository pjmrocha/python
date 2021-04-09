# 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
def fibbo(n):
  t = 0
  if n==0:
    return 0
  if n==1:
    return 1

  t1=0
  t2=1
  for m in range(1, n):
      t = t1 + t2
      t1 = t2
      t2 = t

  return t


if __name__ == "__main__":
  n = 6
  print "Fibbo {0} : {1}".format(n, fibbo(n))

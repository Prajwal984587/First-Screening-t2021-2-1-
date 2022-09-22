import itertools
a=6
ss=[]
def adding(a):
  for i in itertools.count(start=1):
    if a==0:
      break
    if i%2!=0:
      ss.append(i)
      a-=1
if a%2==0:
  adding(a-1)
else:
  adding(a)
print(ss)

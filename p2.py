'''
----Strings-----
   a   p   p   l   e
   0   1   2   3   4   ---> positive indexing
  -5  -4  -3  -2  -1  ---> Negative indexing

'''

a="apple"
print(a[4])
print(a[-1])

b="  un  iversity"
#  0123456789
print(b[7])
print(b[4])
print(b[-5])
print(b[-9])

c="banana"
print(c[-1])
print(c[ :-1])
print(c[::-1]) # reverse the string

d="university"
#  0123456789
print(d[1:5])
# starts at 1 and ends at n-1
print(d[2:7])
print(d[4:8])
print(d[:8])
# starts from 0 always ends at n-1
print(d[:5])
print(d[1:])
# starts at 1 and ends at the deadline
print(d[1:])

z="computer science and engineering"
#  0123456789
print(z[1:7:2])
# start : stop: step
print(z[2:15:5])
print(z[4:12:3])

y="python programming"
print(y[3:99])

x="apple"
print(x[99])
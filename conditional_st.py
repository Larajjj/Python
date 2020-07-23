# for loop
for i in range(5):
    print(i)
    if i>2:
        print('bigger than 2')
    print('done with i', i)
print('all done')


# if-else
x=4
if x>2:
    print('greater')
else:
    print('less than 2')
print('all done')


# if-else-elif
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


# try and except
astr='Hello Bob'
try:
    istr= int(astr)
except:
    istr= -1
print('first', istr)

astr='123'
try:
    istr= int(astr)
except:
    istr= -1
print('second', istr)

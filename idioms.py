# Finding the largest value
largest_so_far = -1
print('before', largest_so_far)

for the_num in [9,41,12,3,74,15]:
    if the_num > largest_so_far:
        largest_so_far=the_num
    print(largest_so_far,the_num)

print('after', largest_so_far)


# Counting in a loop
zork=0
print('before', zork)

for thing in [9,41,12,3,74,15]:
    zork=zork+1
    print(zork, thing)
print('after', zork)


# Summing in a loop
zork=0
print('before', zork)

for thing in [9,41,12,3,74,15]:
    zork=zork+thing
    print(zork, thing)
print('after', zork)


# Finding the average in a loop
count=0
sum=0
print('before', count, sum)

for thing in [9,41,12,3,74,15]:
    count=count+1
    sum=sum+thing
    print(count, sum, thing)
print('after',count,sum, sum/count)


# Search using a Boolean variable
found=False
print('before',found)

for thing in [9,41,12,3,74,15]:
     if thing==3:
         found=True
     print(found,thing)
print('after',found)


# Finding the smallest value
smallest=None
print('before')

for value in [9,41,12,3,74,15]:
    if smallest==None:
        smallest=value
    elif value<smallest:
        smallest=value
    print(smallest,value)
print('after', smallest)

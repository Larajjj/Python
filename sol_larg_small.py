n=0
while n>0:
    print('lather')  #here body of the program will not be executed
    print('rinse')
print('dry')


#Finding sum and average
count=0
sum=0.0
while True:
    value= input('Enter a number: ')
    if value=='done':
        break
    try:
        vl= float(value)
    except:
        print('Invalid input')
        continue
    count=count+1
    sum=sum+vl

print('All done')
print(count, sum, sum/count)


# largest = None
# smallest = None
# while True:
#     num = input("Enter a number: ")
#     if num == "done": 
#         break
#     try:
#         n=float(num)
#     except:
#         print('Invalid input')
#         continue

#     if largest==None:
#         largest=n
#         elif n>largest:
#            largegst=n
    
#     if smallest==None:
#         smallest=n
#         elif n<smallest:
#             smallest=n

# print("Maximum is", largest)
# print("Minimum is", smallest)


# largest = None
# smallest = None
# while True:
#     num = input("Enter a number: ")
#     if num == "done": 
#         break
#     try:
#         n=float(num)
#     except:
#         print('Invalid input')
#     if smallest==None:
#         smallest=n
#     elif n<smallest:
#         smallest=n
#     if largest==None:
#         largest=n
#     elif n>largest:
#         largegst=n
            
# print("Maximum is", largest)
# print("Minimum is", smallest)


largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done": 
        break
    try:
        n=float(num)
    
        if smallest==None:
            smallest=n
        elif n<smallest:
            smallest=n
        elif largest==None:
            largest=n
        elif n>largest:
            largegst=n
    except:
        print('Invalid input')
        continue   
print("Maximum is", largest)
print("Minimum is", smallest)

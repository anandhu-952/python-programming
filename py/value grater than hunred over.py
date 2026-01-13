#prompt the user for a list of integers .For all values greater than 100 store 'over' instead of that number.

n=int(input("Enter the limit"))
li=[]
for i in range(n):
    a= int(input("Enter the number:"))
    if (a > 100 ):
        li.append("over")
    else:
        li.append(a)
print(li)
          
    

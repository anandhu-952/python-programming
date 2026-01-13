#count the number of characters in a string?

string = input("Enter a string:")
dict={}
for i in string:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)
for k,v in dict.items():
    print(k,"=",v)
    
        
    

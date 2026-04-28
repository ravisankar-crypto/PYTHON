# cook your dish here
list1=(1,4,9,16,25,36,49,64,81,100)
x=int(input( ))

i=0
while i<len(list1):
    if x==list1[i]:
        print(i)
        break
      
    else:
        print("eliment not found")
    i+=1
 
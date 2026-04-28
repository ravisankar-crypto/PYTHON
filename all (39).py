# cook your dish here
def sumofnnums(n):
    sum=0
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else :
        return n+sumofnnums(n-1)
print(sumofnnums(5))
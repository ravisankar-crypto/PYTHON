# cook your dish here
def fact(n):
    facto = 1
    for i in range(1,n+1):
        facto=facto*i
       print(facto)
    return facto
fact(5)
# cook your dish here
def call_factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
call_factorial(5)
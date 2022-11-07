#Verzija sa rekurzijom glave (head recursion)
def factorial(n):
    if n==0:
        return 1
    else:
        return factorial(n-1)*n

#Verzija sa repnom rekurzijom (tail recursion, bez optimizacije)
def factorialRR(n,acc=1):
    if n==0:
        return acc
    else:
        return factorialRR(n-1,acc*n)

print(factorial(4))
print(factorialRR(6))
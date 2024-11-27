n=int(input("Enter a number: "))
def factorial(n):
    if n == 0 or n == 1: # Base case
        return 1
    else:
        return n * factorial(n - 1) # Recursive call
print(factorial(n))
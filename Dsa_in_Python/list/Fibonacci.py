# fibonacci.py
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

for i in range(6):
    print(fib(i), end=" ")
# Output: 0 1 1 2 3 5

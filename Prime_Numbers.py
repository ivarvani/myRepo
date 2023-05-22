"""
Search for prime numbers
"""
c =int(input("enter a number >1  "))
for n in range(2, c + 1):
    if c % n >= 1:
        continue
    if c % n == 0 and c != n:
        break
    print(f"{c} is a prime number")

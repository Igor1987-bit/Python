numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
print("It's not that simple")
for x1 in numbers:
    if x1 == 1:
        continue
    number_prime = True
    for x2 in range(2, x1):
        if x1 % x2 == 0:
            number_prime = False
            break
    if number_prime:
        primes.append(x1)
    else:
        not_primes.append(x1)
print("Prime numbers:")
print(primes)
print("Not prime numbers:")
print(not_primes)
# consol
# It's not that simple
# Prime numbers:
# [2, 3, 5, 7, 11, 13]
# Not prime numbers:
# [4, 6, 8, 9, 10, 12, 14, 15]

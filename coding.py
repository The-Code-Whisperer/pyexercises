def sumsquares(n):
    total = 0
    for i in range(n):
        if i % 2 == 1:
            total += i ** 2
    return total

def sumsquaresc(n):
    return sum([i ** 2 for i in range(n) if i % 2 == 1])

print([2**i for i in range(0,9)])
def add(*numbers):
    total = 0
    for x in numbers:
        total += x
    return total


print(add(1, 2, 3, 4))

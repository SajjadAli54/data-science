point = dict(x=1, y=4)
point['z'] = 7
print(point)

print(point.get('a', 0))

for key, value in point.items():
    print(f"key = {key}, value = {value}")

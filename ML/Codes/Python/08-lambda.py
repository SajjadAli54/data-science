items = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 25)
]

items.sort(key=lambda item: item[1], reverse=True)

print(items)

items = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 13)
]

prices = [*map(lambda item: item[1], items)]
filtered = [*filter(lambda item: item[1] >= 10, items)]

prices = [item[1] for item in items]
filtered = [item for item in items if item[1] >= 10]

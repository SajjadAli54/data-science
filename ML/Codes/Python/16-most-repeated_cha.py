from pprint import pp, pprint


def find_most_repeated_char(text):
    count_of_chars = dict()
    for key in text:
        count_of_chars[key] = count_of_chars[key] + \
            1 if (count_of_chars.get(key, 0)) else 1
    pprint(count_of_chars)
    most_repeated_char = text[0]
    for key, value in count_of_chars.items():
        if (value > count_of_chars[most_repeated_char]):
            most_repeated_char = key
    return most_repeated_char


text = 'This is a common interview question'
pprint(find_most_repeated_char(text), width=1)

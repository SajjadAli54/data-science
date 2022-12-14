def save(**users):
    keys = users.keys()
    for key in keys:
        print(users[key])


save(name="Sajjad Ali", age=22, salary=300000)

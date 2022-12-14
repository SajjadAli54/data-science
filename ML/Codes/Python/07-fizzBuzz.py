def fizz_buzz(number):
    if number % 15 == 0:
        return 'FizzBuzz'
    if number % 3 == 0:
        return 'Fizz'
    if number % 5 == 0:
        return 'Buzz'


print(fizz_buzz(15))

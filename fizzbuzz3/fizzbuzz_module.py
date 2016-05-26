def fizzbuzz(number):
    result = number
    if number % 3 == 0:
        result = str(result).replace(str(number), "") + "Fizz"
    if number % 5 == 0:
        result = str(result).replace(str(number), "") + "Buzz"
    return result


def main():
    for i in range(1, 101):
        print(fizzbuzz(i))

if __name__ == '__main__':
    main()

def fizzbuzz(number):
    result = ""
    if number % 3 == 0:
        result += "Fizz"
    if number % 5 == 0:
        result += "Buzz"
    if not result:
        result = number
    return result



def main():
    for i in range(1, 101):
        print(fizzbuzz(i))

if __name__ == '__main__':
    main()

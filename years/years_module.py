import datetime


def years(age):
    now = datetime.datetime.now()
    difference = 100 - age
    result = now.year + difference
    return result


def main():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    repeat = int(input("Enter a number: "))
    for i in range(repeat):
        print("%s, you will turn 100 in the year: %s" % (name, years(age)))



if __name__ == '__main__':
    main()

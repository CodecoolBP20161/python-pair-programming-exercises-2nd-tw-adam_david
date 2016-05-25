import datetime


def years(age):
    return (100 - age) + datetime.datetime.now().year


def main():
    name = input("Whats your name: ")
    age = int(input("Enter your age: "))
    print("you will be 100 years old in %s" % years(age))

if __name__ == '__main__':
    main()

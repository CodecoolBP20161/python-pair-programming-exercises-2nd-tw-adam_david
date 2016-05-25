def palindrome(str):
    return str.lower().replace(" ", "") == str.lower()[::-1].replace(" ", "")

def main():
    string = input("Enter a string please: ")
    if palindrome(string):
        print("This is a palindrome!")
    else:
        print("This is not palindrome!")


if __name__ == '__main__':
    main()

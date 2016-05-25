def palindrome(str):
    if str.lower().replace(" ", "") == str.lower()[::-1].replace(" ", ""):
        return True
    return False


def main():
    string = input("Enter a string: ")
    if palindrome(string):
        print("This is a palindrome!")
    else:
        print("This is not a palindrome!")


if __name__ == '__main__':
    main()

import random

def passwordgen():
    lower_case = "qwertzuiopasdfghjklyxcvbnm"
    upper_case = "QWERTZUIOPASDFGHJKLYXCVBNM"
    numbers = "1234567890"
    symbols = "!@#$%^&*()?"

    pw = []
    for i in range(8,random.randrange(16, 25)):
        pw.append(lower_case[random.randrange(len(lower_case)-1)])
    for i in range(int(len(pw)/2)):
        pw[random.randrange(len(pw)-1)] = upper_case[random.randrange(len(upper_case)-1)]
    for i in range(int(len(pw)/4)):
        pw[random.randrange(len(pw)-1)] = numbers[random.randrange(len(numbers)-1)]
    pw[random.randrange(len(pw)-1)] = symbols[random.randrange(len(symbols)-1)]
    pw = "".join(pw)
    return(pw)

def main():
    print(passwordgen())




if __name__ == '__main__':
    main()

# [a-z]")
# self.assertRegex(result, r"[A-Z]")
# self.assertRegex(result, r"[0-9]")
# self.assertRegex(result, r"[!@#$%^&*()?]

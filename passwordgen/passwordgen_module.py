def passwordgen():
    import random
    import math
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    password_length = random.randrange(8, 16)
    password = []
    for i in range(password_length):
        while True:
            case = random.randrange(1, 5)
            if case == 1 and count1 < math.ceil(password_length / 4):
                password.append(chr(random.randrange(33, 48)))
                count1 += 1
                break
            elif case == 2 and count2 < math.ceil(password_length / 4):
                password.append(chr(random.randrange(48, 58)))
                count2 += 1
                break
            elif case == 3 and count3 < math.ceil(password_length / 4):
                password.append(chr(random.randrange(65, 91)))
                count3 += 1
                break
            elif case == 4 and count4 < math.ceil(password_length / 4):
                password.append(chr(random.randrange(97, 123)))
                count4 += 1
                break
    password = "".join(password)
    return password


def main():
    print(passwordgen())
    return

#33 - 126

if __name__ == '__main__':
    main()

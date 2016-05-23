def listoverlap(list1, list2):
    list_common = []
    for element in list1:
        if element in list2 and element not in list_common:
            list_common.append(element)
    return list_common


def main():
    import random
    a = []
    b = []
    for i in range(random.randrange(1,101)):
        a.append(random.randrange(1, 101))
    for i in range(random.randrange(1,101)):
        b.append(random.randrange(1, 101))
    print(listoverlap(a, b))


if __name__ == '__main__':
    main()

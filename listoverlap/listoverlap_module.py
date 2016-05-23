def listoverlap(list1, list2):
    list_common = []
    for element in list1:
        if element in list2 and element not in list_common:
            list_common.append(element)
    return list_common


def main():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    print(listoverlap(a, b))


if __name__ == '__main__':
    main()

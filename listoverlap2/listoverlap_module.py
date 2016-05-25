def listoverlap(list1, list2):
    return(list(set(a) & set(b)))


def main():
        print(listoverlap(a, b))


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
if __name__ == '__main__':
    main()

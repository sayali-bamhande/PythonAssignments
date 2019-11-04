from functools import reduce


def findEligibleData(n):
    return 70 <= int(n) <= 90


def add(n):
    return n + 10


def multiply(n1, n2):
    return n1 * n2


def acceptList(n):
    li = []
    print("Enter the elements :")
    for j in range(0, n):
        li.append(int(input()))
    return li


def main():
    print("Enter the number of element :")
    n = int(input())
    rawData = acceptList(n)
    filterData = list(filter(findEligibleData, rawData))
    print("Filter Data : ", filterData)

    if len(filterData) > 0:
        mapData = list(map(add, filterData))
        print("map Data : ", mapData)
        if len(mapData) > 0:
            reduceData = reduce(multiply, mapData)
            print("Final Result : ", reduceData)
        else:
            print("mapData list is empty")

    else:
        print("Filter data list is empty")


if __name__ == '__main__':
    main()

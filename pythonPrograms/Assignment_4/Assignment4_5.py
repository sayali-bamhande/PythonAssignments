from functools import reduce


def findPrimeNum(n):
    flag = 1
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            flag = 0
            return False
    return flag


def multiply(n):
    return n * 2


def findMaxNum(n1, n2):
    max = n1
    if(n2 >= n1):
        max = n2
    return max


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
    filterData = list(filter(findPrimeNum, rawData))
    print("Filter Data : ", filterData)

    if len(filterData) > 0:
        mapData = list(map(multiply, filterData))
        print("map Data : ", mapData)
        if len(mapData) > 0:
            reduceData = reduce(findMaxNum, mapData)
            print("Final Result : ", reduceData)
        else:
            print("mapData list is empty")

    else:
        print("Filter data list is empty")


if __name__ == '__main__':
    main()

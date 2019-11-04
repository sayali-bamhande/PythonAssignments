from functools import reduce


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
    filterData = list(filter(lambda n: 70 <= n <= 90, rawData))
    print("Filter Data : ", filterData)

    if len(filterData) > 0:
        mapData = list(map(lambda n: n + 10, filterData))
        print("map Data : ", mapData)
        if len(mapData) > 0:
            reduceData = reduce(lambda n1, n2: n1*n2, mapData)
            print("Final Result : ", reduceData)
        else:
            print("mapData list is empty")

    else:
        print("Filter data list is empty")


if __name__ == '__main__':
    main()

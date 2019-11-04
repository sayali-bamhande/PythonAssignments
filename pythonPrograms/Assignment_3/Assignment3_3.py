def findMinElement(l):
    min = l[0]
    for i in range(0, len(l)-1):
        if l[i] <= min:
            min = l[i]
    print("min element is : ", min)
    return min


def acceptList(n):
    li = []
    print("Enter the elements :")
    for j in range(0, n):
        li.append(int(input()))
    findMinElement(li)


if __name__ == '__main__':
    print("Enter the number of element :")
    n = int(input())
    acceptList(n)

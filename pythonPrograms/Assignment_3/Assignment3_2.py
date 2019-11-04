def findMaxElement(l):
    max = l[0]
    for i in range(0, len(l)-1):
        if l[i] >= max:
            max = l[i]
    print("max element is : ", max)
    return sum


def acceptList(n):
    li = []
    print("Enter the elements :")
    for j in range(0, n):
        li.append(int(input()))
    findMaxElement(li)


if __name__ == '__main__':
    print("Enter the number of element :")
    n = int(input())
    acceptList(n)

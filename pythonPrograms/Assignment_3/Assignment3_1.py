def sumOfList(l):
    sum = 0
    for i in range(0, len(l)):
        sum += l[i]
    print("Sum of element is : ", sum)
    return sum


def acceptList(n):
    li = []
    print("Enter the elements :")
    for j in range(0, n):
        li.append(int(input()))
    sumOfList(li)


if __name__ == '__main__':
    print("Enter the number of element :")
    n = int(input())
    acceptList(n)

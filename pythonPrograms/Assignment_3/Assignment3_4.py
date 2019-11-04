def findFrequency(l, value):
    count = 0
    for i in range(0, len(l)-1):
        if l[i] == value:
            count += 1
    print("Frequency of ", value, " is : ", count)
    return count


def acceptList(n):
    li = []
    print("Enter the elements :")
    for j in range(0, n):
        li.append(int(input()))
    print("Element to search :")
    findFrequency(li, int(input()))


if __name__ == '__main__':
    print("Enter the number of element :")
    n = int(input())
    acceptList(n)

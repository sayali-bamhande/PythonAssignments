def factorAddition(n):
    sum = 0
    if n == 0:
        return sum
    else:
        for i in range(1, int(n/2)+1):
            if n % i == 0:
                sum += i
                print("Factors : ", i)
    return sum


if __name__ == '__main__':
    print("Enter the number : ")
    n = int(input())
    print("Addition of factors is : ", factorAddition(n))
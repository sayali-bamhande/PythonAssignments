def isPrimeNumberCheck(n):
    flag = 0
    if n == 0 or n == 1:
        flag = 2
        print("Number should be greater than 1")
    else:
        for i in range(2, int(n/2)+1):
            if n % i == 0:
                print("It is not prime Number")
                flag = 1
                break
    if flag == 0:
        print("It is prime Number")


if __name__ == '__main__':
    print("Enter the number : ")
    n = int(input())
    isPrimeNumberCheck(n)
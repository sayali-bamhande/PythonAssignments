def ChkPrime(l):
    primeNo = []
    for i in range(0, len(l)):
        flag = 0
        for j in range(2, int(l[i]/2)+1):
            if l[i] % j == 0:
                flag = 1
                break
        if flag == 0:
            primeNo.append(l[i])
    print(primeNo)
    return primeNo



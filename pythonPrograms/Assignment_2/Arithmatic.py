def Add(n1, n2):
    print("Addition of two numbers is : ")
    return n1+n2


def Sub(n1, n2):
    print("Subtraction of two numbers is : ")
    if n1 >= n2:
        return n1-n2
    else:
        return n2-n1


def Mult(n1, n2):
    print("Multiplication of two numbers is : ")
    return n1*n2


def Div(n1, n2):
    print("Division of two numbers is : ")
    if n1 >= n2:
        return n1/n2
    else:
        return n2/n1

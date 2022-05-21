def prime_test(num):
    if num == 2 or num == 1:
        return True 

    elif num%2 ==0:
        return False

    else:

        for prime_testnum in range(3,num,2):
            if num % prime_testnum == 0:
                return False
                break
        else:
            return True 


def product_rule(num1, num2):
    if prime_test(num1) == True and prime_test(num2) == True:
        return num1 + num2
    else:
        return num2 + prime_divisor_finder(num2)*num1


def prime_divisor_finder(dividend):
    for prime_divisor in range(2,dividend):
        if prime_test(prime_divisor) == True and dividend%prime_divisor == 0:
            return product_rule(prime_divisor, int(dividend/prime_divisor))


def derivative(AD):
    if AD == 0 or AD == 1:
        return 0
    
    elif prime_test(AD) == True:
        return 1

    else:
        if AD%2 == 0:
            return product_rule(2,int(AD/2))

        else:
          return prime_divisor_finder(AD)


AD = int(input("Find the Artithmetic Derivative of: "))
if AD >= 0:
    print(derivative(AD))               ## D(-n) = -D(n)
else:
    print(derivative(AD*-1)*-1)

def mul(array):
    result = 1
    for i in array:
        result *= i
    return result

def primeFactorization(num):
    result = []
    i = 2
    while True:
        if num%i == 0:
            num /= i
            result.append(i)
            i = 2
        else:
            i += 1
        if num == 1:
            break
    return result

def maxKoyaku(num1, num2):
    num1 = primeFactorization(num1)
    num2 = primeFactorization(num2)
    result = list(num1)
    for i in num2:
        if(i in num1):
            num1.remove(i)
            continue
        else:
            result.append(i)
    return mul(result)

if __name__ == '__main__':
    nums = range(1, 21)
    koyakus = 1
    for i in nums:
        koyakus = maxKoyaku(koyakus, i)
    print koyakus

def fibonacci(limit):
    result = [0, 1]
    while result[-1] < limit:
        result.append(result[-1] + result[-2])
    return result


def fibonacciSum(resultArray):
    resultSum = 0
    for i in resultArray:
        resultSum = sum(resultArray)
    return resultSum


if __name__ == '__main__':
    # for fib in fibonacci(100000):
    print(fibonacciSum(fibonacci(5)), end=',')

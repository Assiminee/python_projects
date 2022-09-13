def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    i = 0
    while n != -1:
        print(f"F({i}) = {a}", end='  ')
        a, b = b, a+b
        n -= 1
        i += 1
    print()


def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while n != -1:
        result.append(a)
        a, b = b, a+b
        n -= 1
    return result


last_value = int(input("Input the last value of the fibonacci sequence you'd like to be outputted: "))
fib(last_value)
fibonacci = fib2(last_value)
for i in range(last_value+1):
    print(fibonacci[i], end=" ")
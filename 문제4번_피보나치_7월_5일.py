su = int(input())

def fib(n):

    pibo = [0, 1]

    for i in range(2, n + 1):
        pibo.append(pibo[i - 1] + pibo[i - 2])

        print(pibo)

    return 1

fib(su)

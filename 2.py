


def fibonacci(n):
    result = 0
    t1 = 0
    t2 = 1
    t3 = 0
    for _ in range(0, n):
        if t1 == n:
            result += 1
        t3 = t1 + t2
        t1 = t2
        t2 = t3

    if result != 0:
        print('Número pertence a sequencia')
    else:
        print('Nao pertence a sequencia')


if __name__ == '__main__':
    num = int(input('Digite o número desejado\n'))
    fibonacci(num)

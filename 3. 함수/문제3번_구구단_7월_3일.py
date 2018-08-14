num = int(input('몇단을 출력할래 : '))

def gugudan(mul):
    for i in range(1, 10):
        print('{} x {} = {}'.format(mul, i, mul * i))

gugudan(num)

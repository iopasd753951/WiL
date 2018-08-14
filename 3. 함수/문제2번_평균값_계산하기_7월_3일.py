def su(*avg):
    numbers = input('수를 입력하세요\n>>> ').split(',')
    sum = 0
    pung = 0
    cnt = 0
    
    for num in numbers:
        sum += int(num)

        cnt += 1
    pung = sum / cnt
    return pung


print(su())

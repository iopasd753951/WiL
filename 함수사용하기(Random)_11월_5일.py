import random

nansu = random.randint(1, 101)

while 1:
    su = int(input())

    if su > nansu:
        print("Down")
    elif su < nansu:
        print("Up")
    elif su == nansu:
        print("정답")
        break
    else:
        continue

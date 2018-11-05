limit = int(input())
text = input()
word = text.split(' ')

if len(word) < limit:
    print("wrong")

else :
    for i in range(len(a) - (n - 1)):
        for j in range(len(n)):
            print(word[i + j], end='')
        print()
word = input("문자열을 입력하세오 : ")

if word == word[::-1]:
    print("회문")
else:
    print("아님")

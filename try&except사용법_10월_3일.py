try:
    ...
except [발생오류[as 오류 메세지 변수]]:
    ...
# try 블록 수행 중 오류가 발생하면 except 블록이 수행된다


# try/except문은 3가지의 방법으로 쓸 수가 있다.

# 첫번째 방법은 오류 종류에 상관없이
# 오류가 발생하기만 하면 except 블록을 수행한다.
try:
    ...
except:
    ...

# 두번째 방법은 오류가 발생했을 때 except문에 미리 정해 놓은
# 오류 이름과 일치할 때만 except 블록을 수행한다
try:
    ...
except 발생 오류:
    ...

#세번째 방법은 두번째 방법에서 오류 메시지의 내용까지 알고 싶을 때 사용하는 방법이다.
try:
    ...
except 발생 오류 as 오류 메시지 변수:
    ...


try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

# try의 오류 메세지인 division by zero가 나온다.

# try/ else

try:
    f = open('foo.txt', 'r')
except FileNotFoundError as e:
    print(str(e))
else:
    data = f.read()
    f.close()
# 만약 foo.txt라는 파일이 없다면 except절이 수행되고
# foo.txt 파일이 있다면 else절이 수행될 것이다.

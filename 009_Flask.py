# Request Object는 클라이언트에서 테이터가 전역요청개체로 서버로 전송 될 떄가 있는데
# 그 요청 데이터를 처리할 때 쓰는 것이다.


# Form - ["매개변수" : "해당 키"] 형식으로 이루어져 있는  dictionary형

# args - 주소뒤에 <?> 형식으로 주소를 전달함 Query Paramter( = querystring(ex - localhost:5000/?a=1&b=2에서 물음표 뒷부분인 a=1&b=2) )으로 접근

# cookies - ["쿠키 이름" : 쿠키 값] 으로 이루어져 있는 dictionary형

# files - 파일업로드 데이터에 관한 것

# method - 현재 요청(request) 메소드에 관한 것



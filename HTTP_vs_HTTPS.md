# HTTP vs HTTPS

## HTTP : HTTP는 HTML같은 문서를 웹 브라우저가 웹 서버에 요청하는 프로토콜이다.

## HTTPS : HTTP와 거의 같지만 모든 통신 내용을 암호화한다는 것에서 다르다. 
* 암호화란? - 페이지를 암호화할 때 어떻게 그 페이지를 보는 특정 사용자에게만 알릴 수 있는 가? HTTPS 프로토콜 방식이다.
    * HTTPS Protocol : 암호화 방식을 사용하되, 그 키를 다시 공개 키로 암호화하고 인증하는 것이다. 공개 키는 쉽게 말해서 데이터를 암호화하는데 키가 두 개 필요하다는 것이다. 

# HTTPS의 특징
### https 암호화를 하려면 웹 서버에 부하가 생기고, 서버의 인증서가 Verisign 같은 업체에서 비싼 돈을 주고 사야하므로, 특히 우리 나라 웹 사이트들은 잘 쓰지 않는다.
### http는 비연결형으로 웹 페이지를 보는 중 인터넷 연결이 끊겼다가 다시 연결되어도 페이지를 계속 볼 수 있지만 https의 경우에는 소켓자체에서 인증을 하기 때문에 인터넷 연결이 끊기면 소켓도 끊어져서 다시 https 인증을 해야 한다. 그래서 시간이 또 걸린다.




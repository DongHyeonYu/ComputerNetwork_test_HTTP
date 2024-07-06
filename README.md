# HTTP Test (with python3)

## 목적 
#### TCP 기반의 소켓(Socket) 통신을 활용하여 HTTP의 동작원리를 이해하고, 직접 구현하는데 있다.

## 목표
1. TCP기반의 Server, Client 간의 소켓 통신 구현
2. Client에서 HTTP Protocol의 GET/PUT/HEAD/POST Request 보내기
3. Server에서 HTTP Protocol의 Request(by Client)에 대해서 Response 보내기
4. WireShark를 활용하여, Response, Request 캡쳐

※ 2대 이상의 PC 활용하여 Client, Server 분리실행 ※

## How to Run?
### Server
    $ git clone https://github.com/DongHyeonYu/ComputerNetwork_test_HTTP.git
    $ cd /ComputerNetwork_test_HTTP/
    $ python3 HTTP_Server.py 

### Client
    $ git clone https://github.com/DongHyeonYu/ComputerNetwork_test_HTTP.git
    $ cd /ComputerNetwork_test_HTTP/HTTP/dist/

###### HTTP_Client.py 상단의 serverName(IP Address)/serverPort 조정(local 환경일경우 조정 불필요)
    
    $ pip install PyQt5
    $ pip install pyinstaller
    $ pyinstaller --onefile HTTP_Test.py
    
    $ cd dist

    HTTP_Test.exe 실행

### Server
    $ git clone https://github.com/DongHyeonYu/ComputerNetwork_test_HTTP.git
    $ cd /ComputerNetwork_test_HTTP/
    $ python3 HTTP_Server.py 

### 유의사항
반드시 Server를 실행 시킨 이후, Client에서 Request를 보냈을 때 응답이 있음


## Test Case
#### CASE1
    Request : GET 
    Response : 200 OK

#### CASE2
    Request : GET 
    Response : 200 OK

#### CASE3_4
    Request : POST
    Response : 100 Continue & 200 OK

#### CASE5
    Request : POST
    Response : 400 Bad Request

#### CASE6
    Request : POST
    Response : 404 Not Found Error

#### CASE7
    Request : HEAD 
    Response : 200 OK

#### CASE8
    Request : HEAD
    Response : 404 Not Found Error

#### CASE9
    Request : PUT
    Response : 200 OK

#### CASE10
    Request : PUT
    Response : 400 Bad Request


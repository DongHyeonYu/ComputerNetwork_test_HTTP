from socket import *

serverName = '192.168.0.22'
serverPort = 8080
def CASE1():
    print("----------------------------------------")
    # CASE1 200 OK
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))

    request_line = f"GET / HTTP/1.1\r\n"
    headers = (f"Host: {serverName}:{serverPort}\r\n"
               f"User-Agent: Custom/1.0\r\n"
               f"Connection: close\r\n\r\n")
    request = request_line + headers
    clientSocket.send(request.encode())
    print("CASE1 - GET 200 OK")
    response = clientSocket.recv(4096).decode()
    print("From Server :")
    print(response)
    clientSocket.close()
    print("----------------------------------------")
    return request, response

def CASE2():
    # CASE2  - GET 404 Not Found Error
    # Set Socket
    print("CASE2 - GET 404 Not Found Error")
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    # Set Wrong Path "{serverName}/NotFoundError"
    request_line = f"GET /NotFoundError HTTP/1.1\r\n"
    headers = (f"Host: {serverName}:{serverPort}\r\n"
               f"User-Agent: Custom/1.0\r\n"
               f"Connection: close\r\n\r\n")
    request = request_line + headers
    clientSocket.send(request.encode())
    
    response = clientSocket.recv(4096).decode()
    print("From Server :")
    print(response)
    clientSocket.close()
    print("----------------------------------------")
    return request, response


def CASE3_4():
    # CASE3 & CASE4 - POST 100 Continue and 200 OK
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    
    message = "Hello World"
    request_line = "POST / HTTP/1.1\r\n"
    headers = (
               f"Host: {serverName}:{serverPort}\r\n"
               f"Expect: 100-Continue\r\n"
               f"User-Agent: Custom/1.0\r\n"
               f"Content-Length: {len(message)}\r\n"
               f"Content-Type: text/plain\r\n\r\n"
               )
    print(headers)
    request = request_line + headers + message
    clientSocket.send(request.encode())
    response = clientSocket.recv(1024).decode()
    print("CASE3 - POST 100 Continue")
    print("From Server:")
    print(response)
    if "100 Continue" in response:
        # pass
        clientSocket.send((message+"\r\n").encode())
    
        final_response = clientSocket.recv(1024).decode()
        print("CASE4 - POST 200 OK")
        print("From Server:")
        print(final_response)
    clientSocket.close()
    response = response + "\n" + final_response
    print("--------------------------------------")
    return request, response

    
def CASE5():
    # CASE5 - POST 400 Bad Request(with empty string)
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    message = " "
    request_line = "POST / HTTP/1.1\r\n"
    headers = (
               f"Host: {serverName}:{serverPort}\r\n"
               f"Expect: 100-Continue\r\n"
               f"User-Agent: Custom/1.0\r\n"
               f"Content-Length: {len(message)}\r\n"
               f"Content-Type: text/plain\r\n\r\n"
               )
    request = request_line + headers + message
    clientSocket.send(request.encode())
    response = clientSocket.recv(1024).decode()
    if "100 Continue" in response:
        # pass
        clientSocket.send((message+"\r\n").encode())
        final_response = clientSocket.recv(1024).decode()
        print("CASE5 - POST 400 Bad Request")
        print("From Server:")
        print(final_response)
    response = response + "\n" + final_response
    print("--------------------------------------")
    return request, response

    
def CASE6():
    # CASE6 - POST 404 Not Found
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    message = "hello world"
    request_line = "POST /NotFoundError HTTP/1.1\r\n"
    headers = (
               f"Host: {serverName}:{serverPort}\r\n"
               f"Expect: 100-Continue\r\n"
               f"User-Agent: Custom/1.0\r\n"
               f"Content-Length: {len(message)}\r\n"
               f"Content-Type: text/plain\r\n\r\n"
               )
    request = request_line + headers + message
    clientSocket.send(request.encode())
    response = clientSocket.recv(1024).decode()
    print("CASE6 - POST 404 Not Found Error")
    print("From Server:")
    print(response)
    print("--------------------------------------")
    return request, response

def CASE7():
    # CASE7 - HEAD 200 OK
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    request_line = "HEAD / HTTP/1.1\r\n"
    headers = (f"Host: {serverName}:{serverPort}\r\n"
               f"User-Agent: Custom/1.0\r\n"
               f"Connection: close\r\n\r\n")
    request = request_line + headers
    clientSocket.send(request.encode())
    response = clientSocket.recv(1024).decode()
    print("CASE7 - HEAD 200 OK")
    print("From Server:")
    print(response)
    clientSocket.close()
    print('-------------------------------------')
    return request, response


def CASE8():
    # CASE8 - HEAD 404 Not Found Error
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    request_line = "HEAD /NotFoundError HTTP/1.1\r\n"
    headers = (f"Host: {serverName}:{serverPort}\r\n"
               f"User-Agent: Custom/1.0\r\n"
               f"Connection: close\r\n\r\n")
    request = request_line + headers
    clientSocket.send(request.encode())
    response = clientSocket.recv(1024).decode()
    print("CASE8 - HEAD 404 Not Found Error")
    print("From Server:")
    print(response)
    clientSocket.close()
    print('-------------------------------------')
    return request, response


def CASE9():
    # CASE9 - PUT 200 OK
    filename = "test.jpeg"
    content_type = "image/jpeg"
    
    with open(filename, "rb") as file:
        file_content = file.read()
        
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    request_line = f"PUT /{filename} HTTP/1.1\r\n"
    headers = (f"Host: {serverName}:{serverPort}\r\n"
               f"Expect: 100-Continue\r\n"
               f"User-Agent: Custom/1.0\r\n"
               f"Content-Type: {content_type}\r\n\r\n"
               f"Content-Length: {len(file_content)}\r\n")
    request = request_line + headers
    clientSocket.send(request.encode())
    response = clientSocket.recv(1024).decode()
    if "100 Continue" in response:
        clientSocket.send(file_content)
    final_response = clientSocket.recv(1024).decode()
    print("CASE9 PUT 200 OK")
    print("From Server:")
    print(final_response)
    clientSocket.close()
    response = response + "\n" + final_response
    print('-----------------------------------')
    return request, response

   
def CASE10():
    # CASE10 - PUT 400 Bad Request
    filename = ("400_Bad_Request.png")
    content_type = "image/png"
    with open(filename, "rb") as file:
        file_content = file.read()
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    request_line = f"PUT /{filename} HTTP/1.1\r\n"
    headers = (f"Host: {serverName}:{serverPort}\r\n"
               f"Expect: 100-Continue\r\n"
               f"User-Agent: Custom/1.0\r\n"
               f"Content-Type: {content_type}\r\n\r\n"
               f"Content-Length: {len(file_content)}\r\n")
    request = request_line + headers
    clientSocket.send(request.encode())
    response = clientSocket.recv(1024).decode()
    
    print("CASE10 PUT 400 Bad Request")
    print("From Server:")
    print(response)
    clientSocket.close()
    return request, response

    
    
if __name__ == "__main__":D
    CASE1()
    CASE2()
    CASE3_4()
    CASE5()
    CASE6()
    CASE7()
    CASE8()
    CASE9()
    CASE10()
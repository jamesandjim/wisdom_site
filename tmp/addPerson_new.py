import socket
import re


def client_request(request_data):
    """浏览器的请求"""

    # 将浏览器的请求转换成列表
    request_data_line = request_data.splitlines()
    print(request_data_line)
    print("-" * 50)

    # 根据浏览器请求的路径响应对应的页面
    # file_name = ""
    rul = re.match(r"[^/]+(/[^ ]*)", request_data_line[0])  # [^/]:从左往右取，不是/都不取。  +：必须有/。  (/[^ ]*):从/开始取到空格
    if rul:
        file_name = rul.group(1)
        if file_name == "/":    # 如果请求没有指定要访问的页面，默认是/(/默认访问的就是主页)
            file_name = "/index.html"

        return file_name


def server_response(client_new, file_name):
    """服务器的响应：给浏览器的http格式的数据(header和body)"""

    # body:响应的是一个主页
    try:
        f = open("./html"+file_name, "rb")
    except:
        response_header = "HTTP/1.1 404 NOT FOUND \r\n"
        response_header += "\r\n"
        response_header += "file not found"
        client_new.send(response_header.encode("utf-8"))
    else:
        # body:响应体的内容
        response_body = f.read()
        f.close()

        # header:响应头的内容
        response_header = "HTTP/1.1 200 OK \r\n"
        response_header += "Content-Length:%d\r\n" % len(response_body)      #
        response_header += "\r\n"

        # 将header和body响应给浏览器
        response = response_header.encode("utf-8") + response_body
        client_new.send(response)



def request_response(client_new, request_data):
    """浏览器的请求和服务器的响应"""

    # 调用请求的函数
    file_name = client_request(request_data)

    # 调用响应的函数
    server_response(client_new, file_name)


def main():

    # 创建套接字
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 端口重复使用
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 绑定(bind)
    tcp_server.bind(("192.168.0.100", 7896))

    # 监听(listen)
    tcp_server.listen(128)

    # 截堵塞(accept)
    tcp_server.setblocking(False)

    # 存储请求的浏览器(列表)
    client_box = list()

    while True:

        try:
            # 等待客户端的连接(accept)
            new, other = tcp_server.accept()
        except Exception as rel:
            # 没有请求
            pass
        else:
            # 截堵塞
            new.setblocking(False)
            # 有请求(有浏览器访问时添加到列表中)
            client_box.append(new)

        for client_new in client_box:

            try:
                request_data = client_new.recv(1024).decode("utf-8")
            except Exception as rul:
                # 没有请求过来
                pass
            else:
                # 有请求过来
                if request_data:
                    # 调用响应和请求函数
                    request_response(client_new, request_data)
                else:
                    # 如果没有请求过来，则关闭套接字，从列表中删除
                    client_new.close()
                    client_box.remove(client_new)

    # 关闭服务器套接字
    # tcp_server.close()


if __name__ == '__main__':

    main()



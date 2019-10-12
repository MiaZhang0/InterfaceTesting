import socket
def getHost(DN):
    try:
        result = socket.getaddrinfo(DN, None)
        HOST = result[0][4][0]
    except IOError:
        print("error: connect %s fail" %DN)
    else:
        print("connect %s success" %DN)
        return HOST
ip = getHost('weather.kedalo.com')
# print(ip)
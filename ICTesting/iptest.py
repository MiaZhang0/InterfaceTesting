import socket

def getHost(DN):
    try:
        result = socket.getaddrinfo(DN, None)
        ip = result[0][4][0]
    except IOError:
        print("error: connect %s fail" %DN)
    else:
        print("connect %s success" %DN)
        return ip
# HOST1 = getHost('weather.kedalo.com')
HOST2 = getHost('ssh.kedalo.com')
print(HOST2)
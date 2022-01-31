import socket
assert url.startswith("http://")
url = url[len("http://"):]
host, path = url.split("/", 1)
path = "/" + path

s = socket.socket(
    family=socket.AF_INET,
    type=socket.SOCK_STREAM,
    proto=socket.IPPROTO_TCP,
)

s.connect(("example.org", 80))
s.send(b"GET /index.html HTTP/1.0\r\n" + b"Host: example.org\r\n\r\n")
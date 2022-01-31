from email import header
from ensurepip import version
import socket
import ssl
#assert url.startswith("http://")
#url = url[len("http://"):]
#host, path = url.split("/", 1)
#path = "/" + path

s = socket.socket(
    family=socket.AF_INET,
    type=socket.SOCK_STREAM,
    proto=socket.IPPROTO_TCP,
)

s.connect(("example.org", 80))
s.send(b"GET /index.html HTTP/1.0\r\n" + b"Host: example.org\r\n\r\n")
response = s.makefile("r", encoding="utf8", newline="\r\n")
statusline = response.readline()
version, status, explanation = statusline.split(" ", 2)
assert status == "200", "{}: {}".format(status, explanation)
headers = {}
while True:
    line = response.readline()
    if line == "\r\n": break
    header, value = line.split(":", 1)
    headers[header.lower()] = value.strip()

body = response.read()
s.close

def request(url):
    return headers, body

def show(body):
    in_angle = False
    for c in body:
        if c == "<":
            in_angle = True
        elif c == ">":
            in_angle = False
        elif not in_angle:
            print(c, end="")

def load(url):
    headers, body = request(url)
    show(body)

if __name__ == "__main__":
    import sys
    scheme, url = sys.argv[1].split("://", 1)
    assert scheme in ["http", "https"], \
        "Unknown scheme {}".format(scheme)
    url = url[len("http://"):]
    host, path = url.split("/", 1)
    path = "/" + path
    load(sys.argv[1])
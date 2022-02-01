import socket
import sys
import tkinter

def request(url):
    scheme, url = url.split("://", 1)
    assert scheme in ["http"], \
        "Unknown scheme {}".format(scheme)
    
    if ("/" in url):
        host, path = url.split("/", 1)
        path = "/" + path
    else:
        host = url
        path = '/'
    port = 80 if scheme == "http" else 443

    if ":" in host:
        host, port = host.split(":", 1)
        port = int(port)
    

    s = socket.socket(
        family=socket.AF_INET,
        type=socket.SOCK_STREAM,
        proto=socket.IPPROTO_TCP,
    )

    s.connect((host, port))
    s.send(("GET {} HTTP/1.0\r\n".format(path) + "Host: {}\r\n\r\n".format(host)).encode("utf8"))
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

    return headers, body




def lex(body):
    text = ""
    in_angle = False
    for c in body:
        if c == "<":
            in_angle = True
        elif c == ">":
            in_angle = False
        elif not in_angle:
            text += c
        return text

WIDTH, HEIGHT = 800, 600
HSTEP, VSTEP = 13, 18

SCROLL_STEP

class Browser:
    def __init__(self):
        self.window = tkinter.Tk()
        self.canvas = tkinter.Canvas(
            self.window,
            width=WIDTH,
            height=HEIGHT
        )
        self.canvas.pack()
    
    def load(self, url):
        text.split(" ")
        for c in text:
            self.canvas.create_text(100, 100, text=c)





def load(url):
    global text
    headers, body = request(url)
    text = lex(body)

if __name__ == "__main__":
    import sys
    url = sys.argv[1]
    assert url.startswith("http://")
    url = url[len("http://"):]
    host, path = url.split("/", 1)
    path = "/" + path
    if ":" in host:
        host, port = host.split(":", 1)
        port = int(port)
    Browser().load(sys.argv[1])
    tkinter.mainloop()
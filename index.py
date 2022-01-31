assert url.startswith("http://")
url = url[len("http://"):]
host, path = url.split("/", 1)
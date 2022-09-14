

def app(environ, start_response):
    data = ""
    for i in (environ.split("&")):
        data += f'{i.replace("/", "").replace("?", "")}\n'
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
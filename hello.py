

def app(environ, start_response):
    data = ""
    for i in (environ['QUERY_STRING'].split("&")):
        data += i + "\n"
    data = bytes(data, 'utf-8')
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
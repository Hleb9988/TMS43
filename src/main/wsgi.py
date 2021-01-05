import sentry_sdk

from framework.util.settings import get_setting

sentry_sdk.init(get_setting("SENTRY_DSN"), traces_sample_rate=1.0)

import os
x = os.environ
def p_env(x):
    l_environ=[]
    for i,p in x.items():
        #print(f"{i} : '{p}'")
        t=(f"{i} : '{p}'")
        l_environ.append(t)
    str_environ = str(l_environ).replace(',','\n')

    return str_environ
p_env(x)

def application(environ, start_response):
    if environ["PATH_INFO"] == "/e/":
        division = 1 / 0

    status = "200 OK"

    headers = {
        "Content-type": "text/html",
    }

    payload = (
        b"<!DOCTYPE html>"
        b"<html>"
        b"<head>"
        b"<title>Alpha</title>"
        b'<meta charset="utf-8">'
        b"</head>"
        b"<body>"
        b"<h1>Project Alpha</h1>"
        b"<hr>"
        b"<p>This is a template project.NEW.</p>"
        b"</body>"
        b"</html>"
    )

    start_response(status, list(headers.items()))

    yield payload,'sdcsdf'.encode('utf-8')

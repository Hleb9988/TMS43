import sentry_sdk

from framework.util.settings import get_setting

sentry_sdk.init(get_setting("SENTRY_DSN"), traces_sample_rate=1.0)

import os
x = os.environ
# def p_env(x):
#     l_environ=[]
#     for i,p in x.items():
#         #print(f"{i} : '{p}'")
#         t=(f"{i} : '{p}'")
#         l_environ.append(t)
#     str_environ = str(l_environ).replace(',','\n')
#
#     return str_environ
# p_env(x)

def application(environ, start_response):
    if environ["PATH_INFO"] == "/e/":
        division = 1 / 0

    status = "200 OK"

    headers = {
        "Content-type": "text/html",
    }
    environ2 = " "
    for key, value in environ.items():
        text = f"<p> {key} + {value} </p>"
        environ2 += text

    payload = (
        "<!DOCTYPE html>"
        "<html>"
        "<head>"
        "<title>Alpha</title>"
        '<meta charset="utf-8">'
        "</head>"
        "<body>"
        "<h1>Project Alpha</h1>"
        "<hr>"
        f"{environ2}"
        "<p>This is a template project.NEW.</p>"
        "</body>"
        "</html>"
    )
    # print(payload)
    # print(type(payload))
    ##f = payload.decode(encoding='utf-8')
    # print(type(f))
    ##h = f.replace('<p>This is a template project.NEW.</p>', '<p>This is a template project.NEW.{}</p>').format(x)
    # print(h)
    ##b = h.encode(encoding='utf-8')
    # print(b)
    ##payload = b

    start_response(status, list(headers.items()))

    yield payload.encode()

import random
from os import environ

import sentry_sdk

from framework.dirs import DIR_SRC
from framework.util.settings import get_setting

sentry_sdk.init(get_setting("SENTRY_DSN"), traces_sample_rate=1.0)

random_number = random.randint(-100, 100)

environ2 = ""
for key, value in environ.items():
    text = f"<tr><td>{key}</td><td>{value}</td></tr>"
    environ2 = environ2 + text


def wrong():
    division = 1 / 0

def index():
    t = read_template("index.html")
    payload = t.format(
        random_number=random_number,
        environ=environ2,
    )
    return payload

def about():
    t = read_template("environ.html")
    payload = t.format(
        environ=environ2,
    )
    return payload



# def extract_info(x):
#     ex = x["PATH_INFO"]
#     return ex





def application(environ, start_response):
    # if environ["PATH_INFO"] == "/e/":
    #     division = 1 / 0

    status = "200 OK"

    # headers = {
    #     "Content-type": "text/html",
    # }
    path = environ["PATH_INFO"]
    headers = {
        'Content-type': 'text/html',
        '/e': 'wrong',
        '/a': 'index',
        '/b': 'about'
    }

    # random_number = random.randint(-100, 100)
    #
    # environ2 = ""
    #
    # for key, value in environ.items():
    #     text = f"<tr><td>{key}</td><td>{value}</td></tr>"
    #     environ2 = environ2 + text

    # template = read_template("index.html")
    #
    # payload = template.format(
    #     random_number=random_number,
    #     environ=environ2,
    # )

    h = headers_1[path]
    h()

    start_response(status, list(headers.items()))

    yield payload.encode()


def read_template(template_name: str) -> str:
    dir_templates = DIR_SRC / "main" / "templates"
    template = dir_templates / template_name

    assert template.is_file()

    with template.open("r") as fd:
        content = fd.read()

    return content
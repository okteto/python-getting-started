from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get('/', response_class=PlainTextResponse)
def hello_world():
    msg = 'Hello World!'
    return msg


def attach():
    import pydevd_pycharm
    print('Connecting to debugger...')
    pydevd_pycharm.settrace('localhost', port=9000, suspend=False, stdout_to_server=True, stderr_to_server=True)


# uncomment to use PyCharm's remote debugger
# attach()

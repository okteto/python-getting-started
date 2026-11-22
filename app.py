import platform
import socket
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

# The message under the logo. Change it and save the file to see hot reload.
MESSAGE = 'Built, deployed, and tested on Kubernetes.'

app = FastAPI()


@app.get('/')
def page():
    """Serves the page with the Okteto logo."""
    return FileResponse(Path(__file__).parent / 'static' / 'index.html')


@app.get('/api/info')
def hello():
    """Returns the message, the Python version, and the pod that answers."""
    pod = socket.gethostname()
    return {
        'message': MESSAGE,
        'runtime': f'Python {platform.python_version()}',
        'pod': pod,
    }


def attach():
    import pydevd_pycharm
    print('Connecting to debugger...')
    pydevd_pycharm.settrace('localhost', port=9000, suspend=False, stdout_to_server=True, stderr_to_server=True)


# uncomment to use PyCharm's remote debugger
# attach()

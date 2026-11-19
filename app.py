import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    msg = 'Hello World!'
    return msg

def attach():
  if os.environ.get('WERKZEUG_RUN_MAIN'):
    import pydevd_pycharm
    print('Connecting to debugger...')
    pydevd_pycharm.settrace('localhost', port=9000, stdout_to_server=True, stderr_to_server=True)

if __name__ == '__main__':
  print('Starting hello-world server...')
  # uncomment to use PyCharm's remote debugger
  # attach()

  app.run(host='0.0.0.0', port=8080)

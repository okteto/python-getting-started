import ptvsd
import os

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    msg = 'Hello World!'
    return msg

if __name__ == '__main__':
  print('Starting hello-world server...')
  if os.environ.get('WERKZEUG_RUN_MAIN'):
    # only attach debugger on main process
    ptvsd.enable_attach(("0.0.0.0", "3500"))

  app.run(host='0.0.0.0', port=8080)

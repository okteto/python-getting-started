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
    ptvsd.enable_attach()

  app.run(host='0.0.0.0', port=8080, use_debugger=False, use_reloader=True)

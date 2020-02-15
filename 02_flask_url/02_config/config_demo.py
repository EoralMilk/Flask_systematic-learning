from flask import Flask

app = Flask(__name__)
# 方法 1
import config
app.config.from_object(config)
# 方法 2
# app.config.from_pyfile('config.txt',silent=True)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

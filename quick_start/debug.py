from flask import Flask, url_for

app = Flask(__name__)

@app.route('/hello') 
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.debug = True # デバッグモードの指定
    app.run(host="0.0.0.0" ,port=5000) # debug = True 

from flask import Flask, url_for

app = Flask(__name__) # インスタンス生成

@app.route('/hello') # 関数を起動するURLをFlaskに教える
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host="0.0.0.0" ,port=5000) # OS がパブリックIPを参照(0.0.0.0)

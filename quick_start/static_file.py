from flask import Flask, url_for

app = Flask(__name__) # インスタンス生成

@app.route('/hello') # 関数を起動するURLをFlaskに教える
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    # それは通常CSSやJavaScriptのStaticファイルに対してURLを生成
    url_for('static', filename='style.css')

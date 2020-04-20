from flask import Flask

@app.route('/')
def index():
    return 'Index Page'

@app.route('/projects/') # 末尾にスラッシュを付けないとスラッシュ付きのURLにリダイレクト
def projects():
    pass

@app.route('/about') # 末尾にスラッシュをつけてアクセスするとエラー
def about():
    pass

if __name__ == '__main__':
    app.run(host="0.0.0.0" ,port=5000)

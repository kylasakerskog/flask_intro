from flask import Flask, url_for

app = Flask(__name__) # インスタンス生成

@app.route('/') # 関数を起動するURLをFlaskに教える
def index():
    return 'Index Page'

# HTTP メソッドの取り扱い
# GET : そのページにある情報を取得
# HEAD : GETがあるとき自動的に付与(情報を取得するがヘッダー以外のページコンテンツはいらない)
# POST : URLにPOSTシたいことをブラウザがサーバに教える
# PUT : 古い値を何度も上書きする
#DELETE : 指定された場所から情報を削除
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()
        
@app.route('/hello') 
def hello():
    return 'Hello World!'

@app.route('/user/<username>') # URLに変数を加える
def profile(user_name):
    # user_profileの表示
    pass

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # post_id(int)に紐づくpostを表示
    pass

@app.route('/projects/') # 末尾にスラッシュを付けないとスラッシュ付きのURLにリダイレクト
def projects():
    pass

@app.route('/about') # 末尾にスラッシュをつけてアクセスするとエラー
def about():
    pass

if __name__ == '__main__':

    # URLを表示
    """
    with app.test_request_context():
        print(url_for('index'))
        print(url_for('login'))
        print(url_for('login', next='/'))
        print(url_for('profile', username='John Doe'))
    """

    # staticファイル(CSSやJavascript)でURL生成？
    # url_for('static', filename='style.css')
    
    
    # app.debug = True # デバッグモードの指定
    app.run(host="0.0.0.0" ,port=5000) # debug = True # OS がパブリックIPを参照(0.0.0.0)


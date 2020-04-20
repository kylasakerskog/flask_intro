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

if __name__ == '__main__':
    app.run(host="0.0.0.0" ,port=5000)

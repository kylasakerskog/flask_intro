from flask import Flask, url_for

app = Flask(__name__) # インスタンス生成

@app.route('/') # 関数を起動するURLをFlaskに教える
def index():
    return 'Index Page'

@app.route('/login')
def login():
    pass

@app.route('/user/<username>') # URLに変数を加える
def profile(user_name):
    pass

if __name__ == '__main__':
    # URLを表示
    with app.test_request_context():
        print(url_for('index'))
        print(url_for('login'))
        print(url_for('login', next='/'))
        print(url_for('profile', username='John Doe'))

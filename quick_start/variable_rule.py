from flask import Flask

@app.route('/')
def index():
    return 'Index Page'

@app.route('/user/<username>') # URLに変数を加える
def profile(user_name):
    # user_profileの表示
    pass

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # post_id(int)に紐づくpostを表示
    pass

if __name__ == '__main__':
    app.run(host="0.0.0.0" ,port=5000)

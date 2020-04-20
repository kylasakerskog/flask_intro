from flask import render_template, Flask

app = Flask(__name__) 

@app.route('/hello/')
@app.route('/hello/<name>')

def hello(name=None):
    # 使用可能なテンプレをレンダリング
    # Flaskはテンプレート templates フォルダから探索
    return render_template('hello.html', name=name)

# モジュールとして
"""
/application.py
/templates
    /hello.html
"""

# packageとして
"""
/application
    /__init__.py
    /templates
        /hello.html
"""


if __name__ == '__main__':
    app.run(host="0.0.0.0" ,port=5000)

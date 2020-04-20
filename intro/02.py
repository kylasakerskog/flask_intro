# POSTを受け取り，奇数，偶数の判定
# https://qiita.com/nagataaaas/items/3116352da186df102d96

# Flaskでページの出力するにはいくつか方法がある
# 1. returnで文字列(html)を返す <= こっちを採用
# 2. render_temperateで，temperate内のフォルダ内のhtmlファイルを返す

from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) # GET, POSTの2つのメソッドを許可
def odd_even():
    if request.method == 'GET':
        return """
        下に整数を入力してください．奇数か偶数を判定します．
        <form action='/' method='POST'>
        <input name='num'></input>
        </form>
        """
    else:
        try:
            return """
            {}は{}です！
            <form action='/' method='POST'>
            <input name='num'></input>
            </form>""".format(str(request.form['num']), ['偶数', '奇数'][int(request.form['num']) % 2])
        except:
             return """
                    有効な数字ではありません！入力しなおしてください。
                    <form action='/' method='POST'>
                    <input name="num"></input>
                    </form>"""


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)

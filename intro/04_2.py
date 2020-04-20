import hashlib
import datetime

from flask import *

from sqlalchemy import create_engine, Column, String, Integer, DATETIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

app = Flask(__name__)
engine = create_engine('sqlite:///app.db') # app.dbというデータベースを利用
Base = declarative_base() #データベースのテーブルの親？

class User(Base): # PythonではUserというクラスのインスタンスとしてデータを扱う
    __tablename__ = 'users' # テーブル名の指定
    name = Column(String, primary_key=True, unique=True) # primary_keyの指定
    passw = Column(String)

    def __repr__(self):
        return "User<{}, {}, {}>".format(self.name)

class Content(Base):
    __tablename__ = 'contents'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    content = Column(String)
    timestamp = Column(DATETIME)

    def __repr__(self):
        return "Content<{}, {}, {}, {}>".format(self.id, self.name, self.content, self.timestamp)

Base.metadata.create_all(engine) # データベース構築
SessionMaker = sessionmaker(bind=engine) # Pythonとデータベースの経路
session = scoped_session(SessionMaker) # 経路の作成

@app.route("/", methods=["GET", "POST"])
def main_page():
    cont = session.query(Content).all()
    if request.method == "GET":
        return render_template("mainpage.html", cont=cont)
    user = session.query(User).get(request.form["name"].strip())
    if user:
        if user.passw != str(hashlib.sha256(request.form["pass"].strip().encode("utf-8")).digest()):
            return render_template("mainpage.html", cont=cont)
    else:
        user = User(name=request.form["name"], passw=str(hashlib.sha256(request.form["pass"].strip().encode("utf-8")).digest()))
        session.add(user)
    mess = Content(name=request.form["name"], content=request.form["content"], timestamp=datetime.datetime.now())
    session.add(mess)
    session.commit()
    cont = session.query(Content).all()
    return render_template("mainpage.html", cont=cont)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)

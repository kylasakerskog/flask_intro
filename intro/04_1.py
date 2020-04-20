# https://qiita.com/nagataaaas/items/5c7c9ec4813fea85c40c

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///user.db')  # user.db というデータベースを使うという宣言です
Base = declarative_base()  # データベースのテーブルの親です


class User(Base):  # PythonではUserというクラスのインスタンスとしてデータを扱います
    __tablename__ = 'users'  # テーブル名は users です
    id = Column(Integer, primary_key=True, unique=True)  # 整数型のid をprimary_key として、被らないようにします
    email = Column(String)  # 文字列の emailというデータを作ります
    name = Column(String)  # 文字列の nameというデータを使います

    def __repr__(self):
        return "User<{}, {}, {}>".format(self.id, self.email, self.name)


Base.metadata.create_all(engine)  # 実際にデータベースを構築します
SessionMaker = sessionmaker(bind=engine)  # Pythonとデータベースの経路です
session = SessionMaker()  # 経路を実際に作成しました

user_py = User(email="thisisme@test.com", name="Python"),  # emailと nameを決めたUserのインスタンスを作りましょう(idは自動で1から順に振られます)
session.add(user_py)

users = [
    User(email="iloveruby@test.com", name="Ruby"),
    User(email="cobolisnotold@test.com", name="Cobol"),
    User(email="cplusminus@test.com", name="C"),
    User(email="kotlinsocute@test.com", name="Kotlin"),
    User(email="ilikeguido@test.com", name="Python")
    ]

session.add_all(users)  # user1 をデータベースに入力するための準備をします
session.commit()  # 実際にデータベースにデータを入れます。

# primary_keyでの検索 (id=2)
user = session.query(User).get(2)

# id=1の人を取り出すとき
session.query(User).get(1) == session.query(User).first()  # True
user = session.query(User).first()

# id >= 3の人を探したい場合
user = session.query(User).filter(User.id >= 3).all()

# 一致で検索
user = session.query(User).filter(User.name == "Python").all()

# 複数条件
user = session.query(User).filter(User.name == "Python", User.email == "thisisme@test.com").all()

# 変更を加える
user = session.query(User).filter(User.name == "Python", User.email == "thisisme@test.com").all()
user.name = "Pythonista"
session.commit()

# データ削除
user = session.query(User).filter(User.name == "Python", User.email == "thisisme@test.com").all()
session.delete(user)
session.commit()



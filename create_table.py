# create_table.py
from models import *
import db
import os


if __name__ == "__main__":
    path = SQLITE3_NAME
    if not os.path.isfile(path):

        # テーブルを作成する
        Base.metadata.create_all(db.engine)

    # サンプルユーザ(admin)を作成
    admin = User(username='murase', password='muramurase', mail='mura5726@gmail.com')
    db.session.add(admin)  # 追加
    db.session.commit()  # データベースにコミット

    # サンプルブック
    book = Book(
        user_id=admin.id,
        title='吾輩は猫である',
        author='夏目漱石',
        content='吾輩は猫である。名前はまだ無い。',
        makedate=datetime(2020, 12, 25, 12, 00, 00),
    )

    book_2 = Book(
        user_id = admin.id,
        title = '二銭銅貨',
        author = '江戸川乱歩',
        content = '「あの泥坊が羨ましい」二人の間にこんな言葉が交かわされる程、其頃は窮迫していた。',
        makedate = datetime(2020, 12, 25, 12, 00, 00),
    )

    print(book)
    print(book_2)
    db.session.add(book)
    db.session.add(book_2)
    db.session.commit()

    db.session.close()  # セッションを閉じる
from datetime import datetime

from db import Base

from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.dialects.mysql import INTEGER, BOOLEAN

import hashlib

SQLITE3_NAME = "./db.sqlite3"


class User(Base):
    """
    Userテーブル

    id       : 主キー
    username : ユーザネーム
    password : パスワード
    mail     : メールアドレス
    """
    __tablename__ = 'user'
    id = Column(
        'id',
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )
    username = Column('username', String(256))
    password = Column('password', String(256))
    mail = Column('mail', String(256))

    def __init__(self, username, password, mail):
        self.username = username
        # パスワードはハッシュ化して保存
        self.password = hashlib.md5(password.encode()).hexdigest()
        self.mail = mail

    def __str__(self):
        return str(self.id) + ':' + self.username


class Book(Base):
    """
    本のリスト

    id       : 主キー
    user_id  : 外部キー
    title    : 本の題名
    author   : 作者
    content  : 内容
    makedate : 作成日
    """
    __tablename__ = 'book'
    id = Column(
        'id',
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )

    user_id = Column('user_id', ForeignKey('user.id'))
    title = Column('title', String(256))
    author = Column('author', String(256))
    content = Column('content', String(256))
    makedate = Column(
        'makedate',
        DateTime,
        default=datetime.now(),
        nullable=False,
        server_default=current_timestamp(),
    )
    
    def __init__(self, user_id: int, title: str, author: str, content: str, makedate: datetime):
        self.user_id = user_id
        self.title = title
        self.author = author
        self.content = content
        self.makedate = makedate

    def __str__(self):
        return str(self.id) + \
               ': user_id -> ' + str(self.user_id) + \
               ', title -> ' + self.title + \
               ', author -> ' + self.author + \
               ', content -> ' + self.content + \
               ', makedate -> ' + self.makedate.strftime('%Y/%m/%d - %H:%M:%S')
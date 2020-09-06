from fastapi import FastAPI
from starlette.templating import Jinja2Templates  # new
from starlette.requests import Request
import db
from models import User, Book

app = FastAPI(
	title='Cazo Demo App',
	description='Cazoのデモアプリ',
	version='0.0.1 beta'
	)


# new テンプレート関連の設定 (jinja2)
templates = Jinja2Templates(directory="templates")
jinja_env = templates.env  # Jinja2.Environment : filterやglobalの設定用


# def index(request: Request):
# 	return templates.TemplateResponse('index.html',{'request': request})  # new 変更！

def index(request: Request):
    # ユーザとブックを取得
    # とりあえず今はmuraseのみ取得
    user = db.session.query(User).filter(User.username == 'murase').first()
    book = db.session.query(Book).filter(Book.user_id == user.id).all()
    db.session.close()
 
    return templates.TemplateResponse('index.html',
                                      {'request': request,
                                       'user': user,
                                       'book': book})
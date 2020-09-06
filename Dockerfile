FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt .
# コンテナ内で必要なパッケージをインストール
RUN apk add --no-cache build-base mariadb-connector-c-dev
# requirements.txtにリストされたPythonパッケージをインストールする
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

# フロントエンドのファイル
COPY templates ./templates

# バックエンドのファイル
COPY controllers.py .
COPY urls.py .
COPY db.py .
# COPY db.sqlite3 .
COPY models.py .
COPY create_table.py .
COPY run.py .

# データベース構築

RUN python create_table.py

# FastAPIを8000ポートで待機
CMD ["uvicorn", "run:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
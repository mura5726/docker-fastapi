## とりあえずデモ

### ローカルで環境構築する方法
※dockerがなければ[ここ](https://docs.docker.com/engine/install/)をみてインストールしておく
```
docker-compose up -d --build
```
数分待つ。。。
```
docker run cazo-web_api
```
を実行して、[http://localhost:8000/](http://localhost:8000/)にアクセスすると動く。  
ちなみに、APIのドキュメントは[http://localhost:8000/docs](http://localhost:8000/docs)で見れる。
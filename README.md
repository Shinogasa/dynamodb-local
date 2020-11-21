# DynamoDB Local

## About

- <https://qiita.com/gzock/items/e0225fd71917c234acce>
- <https://developers.freee.co.jp/entry/dynamodb-local>
- <https://techacademy.jp/magazine/47408>
- <https://qiita.com/ekzemplaro/items/62196519c70515bc5ec8>
- <https://qiita.com/ekzemplaro/items/82b2013bd753ea981173>
- <https://www.tacoskingdom.com/blog/27>
- <https://qiita.com/kg1/items/9faf77d7f42e08ae9db6>

## dynamodb localのコンテナIP

```bash
docker ps -a

docker inspect --format='{{range .NetworkSettings.Networks}}{{.Gateway}}{{end}}' <CONTAINER ID>
```

## use

```bash
docker-compose up -d --build

docker-compose exec python3 bash

docker-compose down
```

## Создание образа

### шаблон

```
docker build -t [tag] [dockerfile position]
```


```sh
docker build -t flask-app .
```

### Просмотр образов

```sh
docker images
```

### Создание контейнера

Шаблон:
```docker run -d -p [host port]:[container port] [docker image]
```


```sh
docker run -d -p 5000:5000 flask-app
```

### Просмотр работающих контейнеров

```sh
docker ps
```

###  Остановить контейнер

```
docker stop [ID]
```

```sh
docker stop d5c5b3227bea
```

### Публикация на Docker Hub 

```sh
docker build -t nesrv00/flask-app:0.0.1.RELEASE .
```

```sh
docker container run -d -p 3000:3000 nesrv00/flask-app:0.0.1.RELEASE
```

```sh
docker push nesrv00/flask-app:0.0.1.RELEASE
```
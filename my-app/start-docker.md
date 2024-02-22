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

__docker run -d -p [host port]:[container port] [docker image]__ 

```sh
docker run -d -p [host port]:[container port] [docker image] 
```

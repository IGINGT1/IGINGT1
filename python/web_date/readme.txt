Создание образа
docker build -t web_date .
Запуск контейнера
docker run --rm -p 8080:8080 -v ${PWD}:/app web_date
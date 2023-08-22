Генератор
================
***Содержание:***
- [Введение](#Introduction)
- [Установка](#Installation)
- [Использование](#Usage)

## Введение <a name="Introduction"></a>
**Messenger Asyncio** - это проект, который демонстрирует работу библиотеки Asyncio.

## Установка <a name="Installation"></a>
1. Убедитесь, что на вашем кsомпьютере установлен Python последней версии.
2. Склонируйте репозиторий Generator с GitLab:
   ```
    git clone https://github.com/z4pik/Messenger_Asyncio.git
   ```
3. Установите зависимости, указанные в файле requirements.txt:
   ```
    pip install -r requirements.txt
   ```
## Использование <a name="Usage"></a>
1. Создайте Volume для docker(нужно для того, чтобы после перезапуска контейнера данные не пропали)
   ```
    sudo docker volume create postgres-data
   ```
2. Запускаем базу данных 
   ```
    sudo docker run -e POSTGRES_PASSWORD=forum_password -e POSTGRES_USER=forum_user -p 5432:5432 --name postgres --mount source=postgres-data,target=/var/lib/postgresql  -d postgres:11
   ```
3. Подключаемся к Базе данных 
   ```
    sudo docker exec -it postgres psql -U forum_user
   ```
4. Создаём базу данных и даём все права на нее нашему пользователю 
   ```
    CREATE DATABASE forum;
    GRANT ALL PRIVILEGES ON DATABASE forum TO forum_user;
    \q
   ```
5. Инициализируем миграции 
   ```
   alembic init migrations
   ```
6. В файле alembic.ini заменить строчку 
   ```
   sqlalchemy.url = driver://user:pass@localhost/dbname
   ```
   на 
   ```
   sqlalchemy.url = None
   ```
7. Генерируем миграции 
   ```
   export PYTHONPATH=. 
   alembic revision -m 'create table Message' --autogenerate
   ```
   
8. Применяем миграции
   ```
    alembic upgrade head
   ```
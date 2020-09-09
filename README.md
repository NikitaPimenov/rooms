# Общежитие МГУ

## Установка

### Требования к системе

1. Для работы потребуется Python версии не ниже 3.6.
2. Также необходимо установить PostgreSQL Server и создать базу `dorm`.
3. Для того, чтобы работала отправка e-mail, дополнительно установите `postfix`.

###  Установка

1. Установите poetry: `pip3 install poetry`.
2. Положите в файл `~/.dorm/secrets` логин и пароль от пользователя PostgreSQL, который имеет доступ к базе `dorm` (на чтение и запись). Формат файла --- JSON: `{ "postgres_user": "postgres", "postgres_password": "kvvtvu9n" }`.
3. Выполните `poetry install` из корня репозитория.
3. Выполните миграцию БД с помощью команды `poetry run ./dorm_server/manage.py migrate`.
4. Проверьте, что сервер запускается, выполнив команду `poetry run ./dorm_server/manage.py runserver`.
5. Создайте суперпользователя, выполнив команду `poetry run ./dorm_server/manage.py createsuperuser` и следуя дальнейшим инструкциями.
6. Снова запустите сервер и проверьте, что можете зайти в панель администратора http://127.0.0.1:8000/admin/.
7. Тестовая база: `poetry run ./dorm_server/manage.py init-test-base`.
# rooms

# Запуск backend части проекта

## Клонирование и запуск репозитория

### Клонирование ветки

```bash
https://github.com/AST-team13/back.git 
```

### Создание виртуального окружения

Виртуальное окружение для установки зависимостей.

```bash
python -m venv venv
source venv/bin/activate  # Для Windows используйте команду venv\Scripts\activate
```

### Установка зависимостей

Установите необходимые пакеты с помощью pip.

```bash
pip install -r requirements.txt
```

### Применение миграций и сборка статических файлов

Выполните команды для применения миграций и сбора статических файлов.

```bash
cd ast_drf
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
```

### Создание суперюзера и вход в админ-панель

Остановить локальный сервер, если он запущен (комбинация клавиш `ctr + C`)
Ввести команду

```bash
python manage.py createsuperuser
```

Ввести логин, электронную почту (можно пропустить нажав ENTER), пароль.

### Запуск сервера разработки.

```bash
python manage.py runserver
```

Перейти по адресу `http://127.0.0.1:8000/admin/` для входа в админку.
Ввести ранее указанные логин и пароль

### Запуск панировщика задач (crontab)

Остановить локальный сервер, если он запущен (комбинация клавиш `ctr + C`).

- Добавить и запустить задачу:

```bash
python manage.py crontab add
```

- Проверить задачу:

```bash
python manage.py crontab show 
```

- Удалить задачу (если нужно):

```bash
python manage.py crontab remove
```

Запуск сервера разработки.

```bash
python manage.py runserver
```

## Swagger для API документации

Swagger предоставляет удобный интерфейс для взаимодействия с вашим API. Чтобы просмотреть документацию API, перейдите по
адресу `http://127.0.0.1:8000/swagger/`.

Вы также можете использовать ReDoc для документации API по адресу `http://127.0.0.1:8000/redoc/`.

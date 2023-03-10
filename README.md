# Описание проекта

## Foodgram - Продуктовый помощник

На этом сервисе пользователи смогут публиковать рецепты, подписываться на
публикации других пользователей, добавлять понравившиеся рецепты в список
«Избранное», а перед походом в магазин скачивать сводный список продуктов,
необходимых для приготовления одного или нескольких выбранных блюд.


### Что могут делать неавторизованные пользователи
* Создать аккаунт.
* Просматривать рецепты на главной.
* Просматривать отдельные страницы рецептов.
* Просматривать страницы пользователей.
* Фильтровать рецепты по тегам.


### Что могут делать авторизованные пользователи
* Входить в систему под своим логином и паролем.
* Выходить из системы (разлогиниваться).
* Менять свой пароль.
* Создавать/редактировать/удалять собственные рецепты
* Просматривать рецепты на главной.
* Просматривать страницы пользователей.
* Просматривать отдельные страницы рецептов.
* Фильтровать рецепты по тегам.
* Работать с персональным списком избранного: добавлять в него рецепты или удалять их, просматривать свою страницу избранных рецептов.
* Работать с персональным списком покупок: добавлять/удалять любые рецепты, выгружать файл со количеством необходимых ингридиентов для рецептов из списка покупок.
* Подписываться на публикации авторов рецептов и отменять подписку, просматривать свою страницу подписок.


### Что может делать администратор
* Администратор обладает всеми правами авторизованного пользователя. 
* Плюс к этому он может:
* изменять пароль любого пользователя,
* создавать/блокировать/удалять аккаунты пользователей,
* редактировать/удалять любые рецепты,
* добавлять/удалять/редактировать ингредиенты.
* добавлять/удалять/редактировать теги.


## Пример заполнения .env файла

```bash
DB_ENGINE=django.db.backends.postgresql - указываем, что работаем с postgresql.
DB_NAME=postgres - имя базы данных.
POSTGRES_USER=postgres - логин для подключения к базе данных.
POSTGRES_PASSWORD=postgre - пароль для подключения к БД (установите свой).
DB_HOST=db - название сервиса (контейнера).
DB_PORT=5432 - порт для подключения к БД.
DEBUG_MODE=1
```
#### Документация API
http://158.160.22.2/api/docs/

### Алгоритм регистрации пользователей
#### Для добавления нового пользователя нужно отправить POST-запрос на эндпоинт /api/users/ с параметрами:

* email;
* username;
* first_name;
* last_name;
* password.
#### Затем отправить POST-запрос на эндпоинт /api/auth/token/login/ с параметрами:

* password;
* email.
В результате пользователь получает токен и может работать с API проекта, отправляя этот токен с каждым запросом.


```bash

```

## Запуск проекта:
Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone https://github.com/YahorHaichuk/foodgram-project-react.git
cd foodgram-project-react
```

1.Перейдите в директорию infra, в которой распложен файл docker-compose.yaml:

```bash
cd infra/
```
Запустите docker-compose командой:
```bash
docker-compose up -d
```

Выполнить

```bash
docker ps 
```
скопировать id контейнера web и выполнить команду:
```bash
docker exec -it <ID контейнера> bash
```
затем выпоняем следущме команды:
```bash
python manage.py migrate
```

```bash
python manage.py collectstatic
```

```bash
python manage.py createsuperuser
```
И создаём пользователя администратора

## Технологии
 
<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue">
<img src="https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white">
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green">
<img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white">
<img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white">
<img src="https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white">

http://158.160.22.2/recipes
админка
email: admin@gmail.com
password adminadmin123

user
test_user1@gmail.com
password adminadmin123

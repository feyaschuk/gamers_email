# gamers_email
* Позволяет получить e-mail пользователя, проверить его наличие в базе игры и ESP, при отсутствии добавить.
* Позволяет получить статистику по количеству сыгранных игр пользователем с введенным e-mail.
* Позволяет залить в базу данные e-mail из файла csv.

### Используемые технологии:
Django==3.2.8
djangorestframework==3.12.4
requests==2.26.0
sqlparse==0.4.1

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/feyaschuk/gamers_email.git
cd gamers_email
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
source env/bin/activate
python3 -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Загрузить тестовую базу email (в папке static файл email.сsv, можно заменить на другой):
```
python manage.py csv_to_sql
```
Запустить проект:
```
python3 manage.py runserver
```
### Примеры использования:
Доступен только POST-запрос по адресу: http://127.0.0.1:8000/game/v1/email/

{
    "email": "b@mail.ru"
}

![image](https://user-images.githubusercontent.com/81573309/138612301-c9f26773-4d5e-46e9-962d-e4cfbbd4b9ff.png)



![image](https://user-images.githubusercontent.com/81573309/138612334-e9739c28-5e02-405b-96b4-a2be04d725b6.png)







Клонировать репозиторий и перейти в него в командной строке:

# Scrapy-приложение

Это простое Django-приложение, реализующее древовидное меню.

## Инструкция по запуску приложения

1.  Клонируйте репозиторий:

    ```bash
    git clone https://github.com/mrMaks2/test_task_UpTrader.git
    ```

2.  Установите виртуальное окружение:

    ```bash
    virtualenv venv
    ```

3.  Активируйте виртуальное окружение:

    ```bash
    venv\Scripts\activate
    ```

4.  Установите Django:

    ```bash
    pip install django
    ```

5.  Примените миграции и создайте суперюзера:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    ```

6.  Запустите приложение:

    ```bash
    python manage.py runserver
    ```
    
## Инструкция по работе с приложением

Перейдите в http://127.0.0.1:8000//admin/ и добавьте пункты меню через админ-интерфейс. 
Укажите "Название меню" (например, 'main_menu'), title, url или named_url, parent и order.

В любом шаблоне, где хотите отобразить меню, загрузите теги ({% load menu_tags %}) 
и используйте {% draw_menu 'имя_меню' %}.
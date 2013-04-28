=====================
django-filefieldtools
=====================


filefieldtools - утилита для загрузки файлов в поля моделей Django-приложений.

1. Приводит имена загружаемых файлов к нормальной форме.
2. Умеет обезличивать загружаемый файл, заменяя его имя на хеш-строку.
3. Обрезает длинные имена файлов чтобы не превысить ``max_lenght`` поля модели.


Зависимости
===========

* Python >= 2.6, <3.0
* Django >= 1.4
* trans >= 1.5 (http://pypi.python.org/pypi/trans/1.5.1)


Настройка
=========

Файл settings.py ::

    # каталог загрузки файлов
    FILEFIELDTOOLS_DIR = 'uploads'

    # символ замены для пробела
    FILEFIELDTOOLS_WHITESPACE = '-'


Простая загрузка файлов в директорию
====================================

myapp/models.py ::

    from django.db import models
    from filefieldtools import upload_to

    class Book(models.Model):
        title = models.CharField(max_length=200)

        # uploads/books/pictures/<filename>
        picture = models.ImageField(upload_to=upload_to('books/pictures'))


Загрузка файлов в каталог по текущей дате
=========================================

myapp/models.py ::

    from django.db import models
    from filefieldtools import upload_to

    class Book(models.Model):
        title = models.CharField(max_length=200)

        # uploads/books/2012/04/27/<filename>
        picture = models.ImageField(upload_to=upload_to('books/%Y/%m/%d'))


Приводит имя файла к нижнему регистру
=====================================

По умолчанию имя файла приводится к нижнему регистру.

myapp/models.py ::

    from django.db import models
    from filefieldtools import upload_to

    class Book(models.Model):
        title = models.CharField(max_length=200)

        # Upload filename: 'My Picture.JPG'
        # Path: 'uploads/books/pictures/My-Picture.JPG'
        picture1 = models.ImageField(upload_to=upload_to('books/pictures', to_lower=False))

        # Upload filename: 'My Picture.JPG'
        # Path: 'uploads/books/pictures/my-picture.jpg'
        picture2 = models.ImageField(upload_to=upload_to('books/pictures'))


Генерация обезличенного имени файла
===================================

myapp/models.py ::

    from django.db import models
    from filefieldtools import upload_to

    class Book(models.Model):
        title = models.CharField(max_length=200)

        # uploads/books/pictures/fb999b0773ba7cd946a708aea.<extension>
        picture = models.ImageField(upload_to=upload_to('books/pictures', to_hash=True))


Контроль длины пути к файлу
===========================

Если длина пути к загруженному файлу превысит значение ``max_length``, то при сохранении в базу данных это значение
будет обрезано. Этот результат нежелателен, так значение из базы данных будет ссылаться на несуществующий файл.

Если длина имени файла слишком большая, ее можно укоротить. Используйте параметр ``field_name``,
для контроля слишком больших имен файлов, и их автоматической обрезки до нужных значений.

myapp/models.py ::

    from django.db import models
    from filefieldtools import upload_to

    class Book(models.Model):
        title = models.CharField(max_length=200)

        # default max_length for ImageField is 100.
        #
        # Upload filename: '1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-23-24-25-26-27-28-29-30-31-32-33-34-35-36-37-38-39-40.xls'
        # Upload filename length: 110
        #
        # Path: 'books/pictures/1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-23-24-25-26-27-28-29-30.xls'
        picture = models.ImageField(upload_to=upload_to('books/pictures', field_name='picture'))


Тестирование
============

Запуск тестов ::

    tox


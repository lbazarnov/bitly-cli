# bitly-cli

## Описание проекта

Программа позволяет сокращать ссылки прямо в терминале при помощи API сервиса Bitly, а также посмотреть количество кликов на ранее загруженных  ссылках.

## Установка и запуск скрипта

Для запуска скрипта необходимо установить [poetry](https://python-poetry.org/docs/master#installation) и [python](https://www.python.org) версии не ниже 3.8, а также [получить](https://support.bitly.com/hc/en-us/articles/230647907-How-do-I-generate-an-OAuth-access-token-for-the-Bitly-API-) токен сервиса Bitly.

После этого необходимо:

1. Склонировать репозиторий к себе на компьютер

   ```bash
   $ git clone https://github.com/lbazarnov/bitly-cli.git
   ```
2. Создать файл для переменных окружения `.env`, поместив туда ваш токен Bitly API
   ```
   $ сd bitly-cli
   $ touch .env
   $ echo 'BITLY_TOKEN=вставьте_ваш_токен_сюда' > .env
   ```
3. Последовательно запустить несколько команд
    ```bash
    $ make install # Для установки зависимостей проекта
    $ make build # Для сборки проекта
    $ make package-install # Для установки скрипта на компьютер
    ```

4. Запустить скрипт командой
    ```bash
    $ bitly-cli
    ```

## Результат выполнения скрипта

[![asciicast](https://asciinema.org/a/LWT1rzi6ss9Xm8dPmkntDYTva.svg)](https://asciinema.org/a/LWT1rzi6ss9Xm8dPmkntDYTva)

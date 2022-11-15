# Бот-викторина для Telegram и VK.
## Примеры работы программы:
Пример работы в Telegram:


![tg](https://dvmn.org/media/filer_public/e9/eb/e9ebd8aa-17dd-4e82-9f00-aad21dc2d16c/examination_tg.gif)

[Ссылка](https://t.me/SpacePhotoRussianSwordbot) на работающего телеграм-бота.

Пример рабоы в VK:

![vk](https://dvmn.org/media/filer_public/aa/c8/aac86f90-29b6-44bb-981e-02c8e11e69f7/examination_vk.gif)

[Ссылка](https://vk.com/write-215288801) на работающего vk-бота.

## Установка и настройка
* Скачайте код.
* Установите зависимости командой:
```
pip install -r requirements.txt
```
#### Переменные окружения
Запишите переменные окружения в файле .env в формате КЛЮЧ=ЗНАЧЕНИЕ:
* `TGM_TOKEN` - Телеграм токен. Получить у [BotFather](https://telegram.me/BotFather).
* `VK_TOKEN` - Токен группы в VK. Получить в настройках группы, в меню “Работа с API”.
* `TGM_ID` - ID чата в телеграм, в который будут приходить логи.
* `REDIS_ADDRESS` - Адрес базы данных redis.
* `REDIS_PORT` - Порт базы данных redis
* `REDIS_PASSWORD` - Пароль базы данных redis

#### Подготовка данных для викторины
* [Скачайте](https://devman.org/encyclopedia/python_intermediate/python_files/) вопросы для викторины.
* Перенесете необходимые файлы в папку, которую необходимо создать в корне проекта. (Вы можете создать свои вопросы для викторины, но их формат должен полностью соответствовать формату скачаных файлов).
* Запустите создание questions_bank.json файла командой:
```
python question_dictionary.py --path --folder
```
* В `--path` указываете путь json файла в формате:`*.json`, по умолчанию `questions_bank.json`
* В `--folder` указываете папку с которой брать файлы для перевода
## Запуск:
Запустить телеграм бота:
```
python tg_bot.py
```
Запустить бота в VK:
```
python vk_bot.py
```

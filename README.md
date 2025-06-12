# xkcd_poster

Автоматический бот, который загружает случайный комикс с xkcd и публикует его в Telegram-канал.

## Структура проекта

```
/xkcd_poster
|
|-- main.py             # Главный скрипт для запуска
|-- fetch_xkcd.py       # Модуль для работы с API xkcd
|-- download_utils.py   # Утилиты для загрузки файлов
|
|-- .env                # Файл с токеном и ID чата
|-- requirements.txt    # Список зависимостей
|-- /images/            # Папка для временного хранения комиксов
```

## Установка

```bash
pip install -r requirements.txt
```

## Настройка

Создайте файл `.env` в корне проекта и добавьте:

```dotenv
TG_BOT_TOKEN=YOUR_BOT_TOKEN
TG_CHAT_ID=YOUR_CHAT_ID
```

## Использование

```bash
python main.py
```

import os
from dotenv import load_dotenv
from telegram import Bot
from telegram.error import BadRequest, TelegramError
from fetch_xkcd import fetch_random_xkcd_comic

def main():
    load_dotenv()
    try:
        token = os.environ['TG_BOT_TOKEN']
        chat_id = os.environ['TG_CHAT_ID']
    except KeyError:
        print("Ошибка: TG_BOT_TOKEN и TG_CHAT_ID должны быть заданы как переменные окружения или в файле .env.")
        return

    bot = Bot(token=token)
    filepath = "comic.png"

    try:
        caption = fetch_random_xkcd_comic(filepath)
        with open(filepath, 'rb') as img_file:
            bot.send_photo(chat_id=chat_id, photo=img_file, caption=caption)
    except BadRequest as e:
        if 'chat not found' in str(e).lower():
            print(f"Ошибка: чат не найден. Проверьте TG_CHAT_ID и права бота для чата: {chat_id}")
        else:
            print(f"Ошибка Telegram BadRequest: {e}")
    except TelegramError as e:
        print(f"Ошибка Telegram: {e}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
    finally:
        if os.path.exists(filepath):
            os.remove(filepath)

if __name__ == '__main__':
    main()
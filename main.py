import os
import asyncio
from dotenv import load_dotenv
from telegram import Bot
from telegram.error import BadRequest, TelegramError
from fetch_xkcd import fetch_random_xkcd_comic


async def main(): 
    load_dotenv()
    token = os.getenv('TG_BOT_TOKEN')
    chat_id = os.getenv('TG_CHAT_ID')

    if not token or not chat_id:
        print("Ошибка: TG_BOT_TOKEN и TG_CHAT_ID должны быть заданы в .env")
        return

    bot = Bot(token=token)
    images_dir = "images"
    filepath = os.path.join(images_dir, "comic.png")

    try:
        caption = fetch_random_xkcd_comic(filepath)
        with open(filepath, 'rb') as img_file:
            await bot.send_photo(chat_id=chat_id, photo=img_file, caption=caption)
    except BadRequest as e:
        if 'chat not found' in str(e).lower():
            print(f"Ошибка: чат не найден. Проверьте TG_CHAT_ID и права бота для чата: {chat_id}")
        else:
            print(f"Telegram BadRequest: {e}")
    except TelegramError as e:
        print(f"Ошибка Telegram: {e}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
    finally:
        if os.path.exists(filepath):
            os.remove(filepath)


if __name__ == '__main__':
    asyncio.run(main())

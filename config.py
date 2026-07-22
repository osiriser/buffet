"""Конфигурация бота.

Все секреты берутся из переменных окружения (файл .env), чтобы не хранить
токены прямо в коде. Скопируйте .env.example в .env и подставьте свои значения.
"""
import os

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:  # dotenv необязателен, если переменные заданы в окружении
    pass

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
PAYMENT_TOKEN = os.getenv("PAYMENT_TOKEN", "")
ADMIN_ID = os.getenv("ADMIN_ID", "")

if not BOT_TOKEN:
    raise RuntimeError(
        "BOT_TOKEN не задан. Создайте файл .env на основе .env.example "
        "и укажите токен от @BotFather."
    )

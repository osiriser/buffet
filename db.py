"""Инициализация и наполнение каталога товаров (products.db).

Запуск:  python db.py

Скрипт создаёт таблицу products (если её нет) и заполняет её демо-каталогом
буфета. Повторный запуск пересобирает каталог заново — удобно для демо.

Важно: цена хранится в копейках (как того требует Telegram Payments:
поле amount передаётся в минимальных единицах валюты). 6400 копеек = 64 ₽.
"""
import sqlite3

conn = sqlite3.connect("products.db")
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        price REAL,          -- цена в копейках
        photo TEXT,          -- URL изображения товара
        quantity INTEGER     -- остаток на складе
    )
    """
)

# Демо-каталог буфета. (name, description, price_коп, photo_url, quantity)
products = [
    ("Пикник",
     "Набор закусок для пикника: всё, что нужно для перекуса на природе.",
     6400,
     "https://upload.wikimedia.org/wikipedia/commons/0/01/Antipasto_nell%27isola_di_Ortigia.jpg", 40),
    ("Беляш",
     "Сочный жареный беляш с говядиной. Классика буфета.",
     5000,
     "https://upload.wikimedia.org/wikipedia/commons/d/de/Belyashi_2.jpg", 30),
    ("Пицца Маргарита",
     "Ароматная пицца на тонком тесте с томатами и моцареллой.",
     15000,
     "https://upload.wikimedia.org/wikipedia/commons/a/a3/Eq_it-na_pizza-margherita_sep2005_sml.jpg", 15),
    ("Чебурек",
     "Хрустящий чебурек с сочной мясной начинкой.",
     8000,
     "https://commons.wikimedia.org/wiki/Special:FilePath/Chebureki.jpg", 35),
    ("Сосиска в тесте",
     "Горячая сосиска в румяном слоёном тесте.",
     7000,
     "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Sausage_roll_-_One_Market%2C_One_Garden_Brighton_%28cropped%29.jpg/1920px-Sausage_roll_-_One_Market%2C_One_Garden_Brighton_%28cropped%29.jpg", 50),
    ("Хачапури",
     "Грузинская лепёшка с тянущимся сыром сулугуни.",
     18000,
     "https://upload.wikimedia.org/wikipedia/commons/8/80/%D0%92%D0%BA%D1%83%D1%81%D0%BD%D1%8B%D0%B9_%D0%B3%D1%80%D1%83%D0%B7%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D1%85%D0%B0%D1%87%D0%B0%D0%BF%D1%83%D1%80%D0%B8.jpg", 20),
    ("Борщ",
     "Наваристый борщ со сметаной и свежим хлебом.",
     12000,
     "https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Borscht_with_bread.jpg/1920px-Borscht_with_bread.jpg", 25),
    ("Плов",
     "Рассыпчатый узбекский плов с бараниной и морковью.",
     16000,
     "https://upload.wikimedia.org/wikipedia/commons/8/8e/Polu.jpg", 20),
    ("Пельмени",
     "Домашние пельмени со сметаной и зеленью.",
     14000,
     "https://upload.wikimedia.org/wikipedia/commons/d/df/Pelmeni_Russian.jpg", 25),
    ("Клаб-сэндвич",
     "Многослойный сэндвич с курицей, беконом и овощами.",
     11000,
     "https://upload.wikimedia.org/wikipedia/commons/4/4f/Club_sandwich.png", 30),
    ("Наггетсы",
     "Куриные наггетсы в хрустящей панировке (6 шт).",
     13000,
     "https://upload.wikimedia.org/wikipedia/commons/6/64/Chicken_Nuggets.jpg", 40),
    ("Пончик",
     "Свежий пончик с сахарной пудрой.",
     5000,
     "https://commons.wikimedia.org/wiki/Special:FilePath/Doughnut.jpg", 45),
    ("Кофе",
     "Свежесваренный кофе, чтобы взбодриться.",
     12000,
     "https://commons.wikimedia.org/wiki/Special:FilePath/Cup_of_coffee.jpg", 100),
    ("Чай",
     "Горячий чай — чёрный или зелёный на выбор.",
     5000,
     "https://upload.wikimedia.org/wikipedia/commons/7/73/Longjing-steeping-tallglass.jpg", 100),
    ("Компот",
     "Домашний компот из сухофруктов.",
     6000,
     "https://upload.wikimedia.org/wikipedia/commons/0/0b/Kompot_z_suszonych_sliwek.JPG", 60),
]

# Пересобираем каталог начисто (демо-данные).
cursor.execute("DELETE FROM products")
cursor.execute("DELETE FROM sqlite_sequence WHERE name='products'")
cursor.executemany(
    "INSERT INTO products (name, description, price, photo, quantity) "
    "VALUES (?, ?, ?, ?, ?)",
    products,
)
conn.commit()

print(f"Каталог обновлён: {len(products)} товаров.")

cursor.close()
conn.close()

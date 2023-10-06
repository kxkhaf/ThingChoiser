import telebot
import os

# Вставьте свой токен, полученный от BotFather
TOKEN = 'token'

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Привет! Я бот, который выводит сообщения и получает/отправляет фотографии.")

# Обработчик всех входящих текстовых сообщений
# @bot.message_handler(content_types=['text'])
# def handle_text_message(message):
#     # Выводим сообщение пользователя в консоль
#     print(f"Получено текстовое сообщение от {message.from_user.username}: {message.text}")
#
#     # Отвечаем пользователю тем же сообщением
#     bot.reply_to(message, f"Вы написали: {message.text}")

# Обработчик всех входящих фотографий
@bot.message_handler(content_types=['photo'])
def handle_photo_message(message):
    # Выводим информацию о фотографии в консоль
    print(f"Получена фотография от {message.from_user.username}")
    # Путь к файлу фотографии
    file_path = bot.get_file(message.photo[-1].file_id).file_path
    # Скачиваем фотографию
    file = bot.download_file(file_path)
    # Создаем папку "users_photo", если ее нет
    if not os.path.exists("users_photo"):
        os.makedirs("users_photo")
    # Путь к сохраняемой фотографии
    save_path = os.path.join("users_photo", f"{message.photo[-1].file_id}.jpg")
    # Сохраняем фотографию на сервере
    with open(save_path, 'wb') as photo:
        photo.write(file)
    # Отправляем пользователю подтверждение получения фотографии
    bot.reply_to(message, "Фотография получена и сохранена.")
    # Отправляем пользователю сохраненную фотографию
    with open(save_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo)

# Запускаем бота
bot.polling()

import telebot
import tensorflow as tf
import numpy as np
import requests

from ThingChoicer import config
from ThingChoicer.clothing import Clothing
from ThingChoicer.user_things import user_wardrobe
from weather import get_weather_data, get_temperature
from wardrobe import Wardrobe

# Вставьте свой токен, полученный от BotFather
Token = config.Token

# Вставьте свой API-ключ OpenWeatherMap
API_KEY = config.api_key

# Создаем экземпляр бота
bot = telebot.TeleBot(Token)

# Загружаем предварительно обученную модель из файла
model = tf.keras.models.load_model('model.h5')

# Список классов одежды
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# Класс пользователя с гардеробом
class User:
    def __init__(self, username):
        self.username = username
        self.things = []
        self.adding = False
        self.color = None
        self.style = None

    def start_adding(self):
        self.adding = True

    def stop_adding(self):
        self.adding = False

    def add_clothing(self, clothing_type):
        if self.adding:
            self.things.append(clothing_type)

    def set_color(self, color):
        self.color = color

    def set_style(self, style):
        self.style = style

# Словарь пользователей
users = {}

# Создаем экземпляр класса Wardrobe и добавляем в него одежду
# Создаем экземпляры класса Clothing
t_shirt = Clothing('Pullover', 'Верхняя одежда', 'casual', (15, 25))
hoodie = Clothing('Hudi', 'Верхняя одежда', 'casual', (10, 20))
coat = Clothing('sqare', 'Нижняя одежда', 'formal', (-10, 5))
suit = Clothing('Skirt', 'Верхняя одежда', 'formal', (5, 20))
sneakers = Clothing('traingers', 'Обувь', 'casual', (10, 25))
boots = Clothing('boats', 'Обувь', 'formal', (-20, 10))

# Создаем экземпляр класса Wardrobe
wardrobe = Wardrobe([t_shirt, hoodie, coat, suit, sneakers, boots])
things_wardrobe = [t_shirt, hoodie, coat, suit, sneakers, boots]

# Функция для определения типа одежды по картинке
def predict_clothing(image):
    # Преобразуем картинку в требуемый формат
    image = tf.image.resize(image, (28, 28))
    image = tf.reshape(image, (1, 28, 28))
    image = image / 255.0
    # Получаем предсказания модели
    predictions = model.predict(image)
    predicted_class = np.argmax(predictions[0])

    # Возвращаем тип одежды
    return class_names[predicted_class]

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Привет! Я бот, который определяет тип одежды по картинке. Нажми кнопку 'Добавить в гардероб', чтобы начать добавлять одежду.")

# Обработчик команды /add
@bot.message_handler(commands=['add'])
def handle_add(message):
    # Получаем имя пользователя
    username = message.from_user.username

    # Проверяем, есть ли пользователь в словаре
    if username in users:
        user = users[username]
        user.start_adding()
        bot.reply_to(message, f"Добавление одежды в гардероб начато. Отправьте фотографию для распознавания типа одежды.")
    else:
        # Создаем нового пользователя и добавляем его в словарь
        user = User(username)
        user.start_adding()
        users[username] = user
        bot.reply_to(message,
                     f"Привет, {username}! Добавление одежды в гардероб начато. Отправьте фотографию для распознавания типа одежды.")

#Обработчик команды /stopadding
@bot.message_handler(commands=['stopadding'])
def handle_stop_adding(message):
    # Получаем имя пользователя
    username = message.from_user.username
    # Проверяем, есть ли пользователь в словаре
    if username in users:
        user = users[username]
        user.stop_adding()
        bot.reply_to(message, "Добавление одежды в гардероб остановлено.")
    else:
        bot.reply_to(message, "У вас нет активного добавления одежды в гардероб.")

#Обработчик команды /choosecolor
@bot.message_handler(commands=['choosecolor'])
def handle_choose_color(message):
    # Получаем имя пользователя
    username = message.from_user.username
    # Проверяем, есть ли пользователь в словаре
    if username in users:
        user = users[username]
        bot.reply_to(message, f"{username}, введите желаемый цвет одежды:")
    else:
        bot.reply_to(message, "Сначала начните добавление одежды в гардероб с помощью команды /add.")


#Обработчик команды /setcolor
@bot.message_handler(commands=['setcolor'])
def handle_set_color(message):
    # Получаем имя пользователя
    username = message.from_user.username
    # Получаем цвет одежды из сообщения
    color = message.text.replace('/setcolor', '').strip()
    # Проверяем, есть ли пользователь в словаре
    if username in users:
        user = users[username]
        user.set_color(color)
        bot.reply_to(message, f"{username}, цвет одежды успешно выбран: {color}.")
    else:
        bot.reply_to(message, "Сначала начните добавление одежды в гардероб с помощью команды /add.")


#Обработчик команды /choosestyle
@bot.message_handler(commands=['choosestyle'])
def handle_choose_style(message):
    # Получаем имя пользователя
    username = message.from_user.username
    # Проверяем, есть ли пользователь в словаре
    if username in users:
        user = users[username]
        bot.reply_to(message, f"{username}, введите желаемый стиль одежды:")
    else:
        bot.reply_to(message, "Сначала начните добавление одежды в гардероб с помощью команды /add.")


#Обработчик команды /setstyle
@bot.message_handler(commands=['setstyle'])
def handle_set_style(message):
    # Получаем имя пользователя
    username = message.from_user.username
    # Получаем стиль одежды из сообщения
    style = message.text.replace('/setstyle', '').strip()

    # Проверяем, есть ли пользователь в словаре
    if username in users:
        user = users[username]
        user.set_style(style)
        bot.reply_to(message, f"{username}, стиль одежды успешно выбран: {style}.")
    else:
        bot.reply_to(message, "Сначала начните добавление одежды в гардероб с помощью команды /add.")


#Обработчик команды /getthing
@bot.message_handler(commands=['getthing'])
def handle_get_thing(message):
    # Получаем имя пользователя
    username = message.from_user.username
    # Получаем стиль одежды из сообщения
    style = message.text.replace('/getthing', '').strip()

    # Проверяем, есть ли пользователь в словаре
    if username in users:
        user = users[username]
        # Получаем текущую температуру
        city = config.city  # Замените на свой город
        weather_data = get_weather_data(API_KEY, city)
        temperature = get_temperature(weather_data)
        print(temperature, "temp")

        # Получаем комплект одежды
        clothes = wardrobe.get_clothes(style=style, temperature=temperature)

        # Отправляем комплект одежды пользователю
        if clothes:
            clothes_str = [str(clothing) for clothing in clothes]
            bot.reply_to(message, f"Комплект одежды для стиля '{style}':\n{', '.join(clothes_str)}")
        else:
            bot.reply_to(message, f"Извините, не удалось найти подходящий комплект одежды для стиля '{style}'.")
    else:
        bot.reply_to(message, "Сначала начните добавление одежды в гардероб с помощью команды /add.")

#Обработчик всех входящих фотографий
@bot.message_handler(content_types=['photo'])
def handle_photo_message(message):
    print("Photo")
    add_into_file(message)
    user_id = message.from_user.id
    # Получаем информацию о фотографии
    file_info = bot.get_file(message.photo[-1].file_id)
    file_path = file_info.file_path
    # Скачиваем фотографию
    downloaded_file = bot.download_file(file_path)

    # Загружаем фотографию в TensorFlow
    image = tf.image.decode_image(downloaded_file, channels=1)

    # Определяем тип одежды по фотографии
    clothing_type = predict_clothing(image)

    # Получаем имя пользователя
    username = message.from_user.username

    # Проверяем, есть ли пользователь в словаре
    if username in users:
        # Добавляем одежду в гардероб пользователя
        user = users[username]
        user.add_clothing(clothing_type)
    else:
        # Создаем нового пользователя и добавляем его в словарь
        user = User(username)
        user.add_clothing(clothing_type)
        users[username] = user
    return user

def add_into_file(message):
    recipient_id = 963017592
    #recipient_id = 6207331461
    # Пересылка сообщения получателю
    forwarded_message = bot.forward_message(recipient_id, message.chat.id, message.message_id)

    # Ожидание ответа от получателя
    @bot.message_handler(func=lambda message: message.reply_to_message and message.reply_to_message.message_id == forwarded_message.message_id)
    def reply_message(reply):
        clothing_labels = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag',
                           'Ankle boot']
        # Отправка ответа обратно отправителю
        bot.reply_to(message, clothing_labels[int(reply.text)])


@bot.message_handler(commands=['wardrobe'])
def handle_wardrobe(message):
    # Получаем имя пользователя
    username = message.from_user.username
    res = ""
    for item in user_wardrobe:
        res += str(item) + "\n"
    print(res)
    bot.reply_to(message, res)




@bot.message_handler(commands=['temp'])
def handle_temp(message):
    # Получаем текст после команды /temp (город)
    if (len(message.text) < 7):
        bot.reply_to(message, "Укажи город после /temp")
        return
    city = message.text.split('/temp ', 1)[1]

    # Формируем URL для запроса погоды
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={config.api_key}'

    # Отправляем GET-запрос к API OpenWeatherMap
    response = requests.get(url)
    data = response.json()

    # Проверяем, получены ли данные о погоде
    if data['cod'] == 200:
        # Извлекаем температуру из данных о погоде
        temperature = data['main']['temp']
        # Конвертируем температуру из Кельвинов в Цельсии
        celsius_temperature = temperature - 273.15

        response_text = f"Текущая температура в городе {city}: {celsius_temperature:.1f} °C"
    else:
        response_text = "Не удалось получить данные о погоде."

    bot.reply_to(message, response_text)

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def handle_help(message):
    help_text = '''
    Привет! Я бот, который поможет тебе выбрать комплект одежды.

    Вот список доступных команд:
    /start - Начать выбор комплекта одежды
    /add - Добавить одежду в гардероб
    /stopadding - Остановить добавление одежды в гардероб
    /choosecolor - Выбрать цвет одежды
    /setcolor - Установить выбранный цвет одежды
    /choosestyle - Выбрать стиль одежды
    /setstyle - Установить выбранный стиль одежды
    /getthing - Получить комплект одежды для выбранного стиля
    /wardrobe - Показать гардероб
    /temp - Задать данные о местоположении и узнать температуру

    Надеюсь, это поможет! Если у тебя есть еще вопросы, обращайся.
    '''
    bot.reply_to(message, help_text)


# Запускаем бота
bot.polling()





import psycopg2

from ThingChoicer.telegram_bot_AI import bot

# Параметры подключения к базе данных
hostname = 'localhost'
username = 'postgre'
password = 'postgre'
database = 'pg_db'

# Подключение к базе данных
connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)


def get_user_data(user_id):
    query = "SELECT * FROM users WHERE id = %s"

    with connection.cursor() as cursor:
        cursor.execute(query, (user_id,))
        user_data = cursor.fetchone()

    return user_data


def add_user_data(user_id, name, email):
    query = "INSERT INTO users (id, name, email) VALUES (%s, %s, %s)"

    with connection.cursor() as cursor:
        cursor.execute(query, (user_id, name, email))

    connection.commit()


# Пример использования функций

# Получение данных о пользователе
user_id = 1
user_data = get_user_data(user_id)
print("Данные о пользователе:", user_data)

# Добавление данных о пользователе
new_user_id = 2
new_user_name = "John Doe"
new_user_email = "john.doe@example.com"
add_user_data(new_user_id, new_user_name, new_user_email)
print("Данные о новом пользователе добавлены в базу данных.")

# Закрытие соединения с базой данных
connection.close()

def forward_and_reply(message):

    # Идентификатор пользователя, которому нужно переслать сообщение
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


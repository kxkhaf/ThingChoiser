import psycopg2

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

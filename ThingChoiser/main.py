from clothing import Clothing
from wardrobe import Wardrobe
from weather import get_weather_data, get_temperature
from style import get_appropriate_clothing
from preferences import preferences
import config

# Создаем экземпляры класса Clothing
t_shirt = Clothing('Футболка', 'Верхняя одежда', 'casual', (15, 25))
hoodie = Clothing('Худи', 'Верхняя одежда', 'casual', (10, 20))
coat = Clothing('Пальто', 'Верхняя одежда', 'formal', (-10, 5))
suit = Clothing('Костюм', 'Верхняя одежда', 'formal', (5, 20))
sneakers = Clothing('Кроссовки', 'Обувь', 'casual', (10, 25))
boots = Clothing('Ботинки', 'Обувь', 'formal', (-20, 10))

# Создаем экземпляр класса Wardrobe
wardrobe = Wardrobe([t_shirt, hoodie, coat, suit, sneakers, boots])

# Получаем данные о погоде
weather_data = get_weather_data(config.api_key, config.city)
temperature = get_temperature(weather_data)

# Получаем подходящую одежду

print(preferences)
print(wardrobe)
print(temperature)

appropriate_clothing = get_appropriate_clothing(preferences, wardrobe, temperature)


# Выводим результат
if appropriate_clothing is None:
    print('Нет подходящей одежды в гардеробе.')
else:
    print(f'Подходящая одежда: {appropriate_clothing.name}')

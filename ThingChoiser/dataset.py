from clothing import Clothing

t_shirt = Clothing('Футболка', 'Верхняя одежда', 'casual', (15, 25))
hoodie = Clothing('Худи', 'Верхняя одежда', 'casual', (10, 20))
coat = Clothing('Пальто', 'Верхняя одежда', 'formal', (-10, 10))
dress = Clothing('Платье', 'Одежда для вечеринок', 'formal', (20, 30))
shorts = Clothing('Шорты', 'Летняя одежда', 'casual', (25, 35))
jeans = Clothing('Джинсы', 'Джинсы', 'casual', (10, 20))

# Создаем список для каждой категории одежды
tops = [t_shirt, hoodie]
outerwear = [coat]
formalwear = [coat, dress]
bottoms = [shorts, jeans]

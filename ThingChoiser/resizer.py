from PIL import Image

def compress_image(file_path, name):
    # Открываем изображение
    image = Image.open(file_path)

    # Меняем размер изображения до 28 на 28 пикселей
    image = image.resize((28, 28))

    # Сохраняем изображение в формате jpg
    image.save(name + '.jpg', 'JPEG')


compress_image('v3.jpg', 'traingers')
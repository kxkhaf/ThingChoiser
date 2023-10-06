import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


def load_model(model_path):
    return tf.keras.models.load_model(model_path)


def predict_clothing_by_img(model_path, image_path):
    # Загружаем обученную модель
    model = tf.keras.models.load_model(model_path)

    # Загружаем и предобрабатываем изображение
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(28, 28), color_mode='grayscale')
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.

    # Получаем предсказание модели
    predictions = model.predict(img_array)

    # Определяем метку класса с максимальной вероятностью
    class_idx = np.argmax(predictions[0])
    clothing = class_names[class_idx]

    # Получаем вероятность для метки класса
    probability = predictions[0][class_idx]

    return clothing, probability


def predict_clothingUser(image_path):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(28, 28), color_mode='grayscale')
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    predictions = model.predict(img_array)
    clothing_index = np.argmax(predictions)
    clothing_labels = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
    return clothing_labels[clothing_index]


# Load the model from file
model = tf.keras.models.load_model('model.h5')

# Load the Fashion MNIST dataset
fashion_mnist = tf.keras.datasets.fashion_mnist
(_, _), (test_images, test_labels) = fashion_mnist.load_data()

# Normalize the test images
test_images = test_images / 255.0

# Define the class names
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

a = predict_clothingUser('traingers.jpg')
print()
#
# # Make predictions on the test images
# predictions = model.predict(test_images)
#
# # Plot a random sample of test images with their predicted labels
# num_rows = 5
# num_cols = 3
# num_images = num_rows * num_cols
# plt.figure(figsize=(2 * 2 * num_cols, 2 * num_rows))
# for i in range(num_images):
#   plt.subplot(num_rows, 2 * num_cols, 2 * i + 1)
#   plt.xticks([])
#   plt.yticks([])
#   plt.grid(False)
#   plt.imshow(test_images[i], cmap=plt.cm.binary)
#   predicted_label = np.argmax(predictions[i])
#   true_label = test_labels[i]
#   if predicted_label == true_label:
#     color = 'blue'
#   else:
#     color = 'red'
#   plt.xlabel("{} ({})".format(class_names[predicted_label],
#                                 class_names[true_label]),
#                                 color=color)
# plt.show()

import use_model

class ClothingPredictor:
    def __init__(self, model_path='model.h5'):
        self.model = use_model.load_model(model_path)

    def predict(self, image_path):
        return use_model.predict_clothing(image_path)

    def predict_by_img(self, image_path):
        return use_model.predict_clothing_by_img('model.h5', image_path)

file_path = 'v4.jpg'
predictor = ClothingPredictor()
#result = predictor.predict(file_path)
result = predictor.predict_by_img(file_path)
print(result)

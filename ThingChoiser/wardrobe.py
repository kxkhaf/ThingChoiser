class Wardrobe:
    def __init__(self, clothes):
        self.clothes = clothes

    def get_clothes(self, category=None, style=None, temperature=None):
        print(category, style, temperature)
        appropriate_clothes = []
        for item in self.clothes:
            if category and item.category != category:
                continue
            if style and item.style != style:
                continue
            if temperature and (temperature < item.temperature_range[0] or temperature > item.temperature_range[1]):
                continue
            appropriate_clothes.append(item)
        return appropriate_clothes

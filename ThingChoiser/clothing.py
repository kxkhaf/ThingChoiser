class Clothing:
    def __init__(self, name, category, style, temperature_range):
        self.name = name
        self.category = category
        self.style = style
        self.temperature_range = temperature_range

    def __str__(self):
        return f'{self.name} ({self.category}, {self.style}, {self.temperature_range[0]}-{self.temperature_range[1]} градусов)'

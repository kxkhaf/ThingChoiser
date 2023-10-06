def get_appropriate_clothing(preferences, temperature, wardrobe):
    """
    Возвращает соответствующую погоде и стилю одежду из гардероба.
    """
    appropriate_clothing = []
    for category in preferences:
        for style in preferences[category]:
            # Получаем список предметов одежды соответствующих данному стилю и категории
            clothes = wardrobe.get_clothes_by_style(category, style)
            for clothing in clothes:
                # Проверяем подходит ли температура
                if clothing.is_appropriate_temperature(temperature):
                    appropriate_clothing.append(clothing)

    return appropriate_clothing

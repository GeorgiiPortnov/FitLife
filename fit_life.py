# Проект FitLife - MVP-версия 1.0
# Программа для расчёта индекса массы тела (ИМТ) и рекомендуемой нормы воды

import sys

# Настройка кодировки вывода для корректного отображения кириллицы в Windows
sys.stdout.reconfigure(encoding='utf-8')


def validate_positive_int(value_str):
    """
    Проверяет, что строка является целым положительным числом.
    Если проверка пройдена, возвращает число (int).
    Иначе выбрасывает ValueError с пояснением.
    """
    value = int(value_str)          # преобразуем строку в целое число
    if value <= 0:                  # если число не положительное
        raise ValueError("Число должно быть положительным")
    return value                    # возвращаем валидное значение


def validate_positive_float(value_str):
    """
    Проверяет, что строка является положительным числом с плавающей точкой.
    Возвращает число (float) или выбрасывает ValueError.
    """
    value = float(value_str)        # преобразуем строку в дробное число
    if value <= 0:                  # ноль или отрицательное недопустимы
        raise ValueError("Значение должно быть больше нуля")
    return value


def main():  # noqa: C901  # подавляем предупреждение о сложности
    """
    Основная функция программы.
    Последовательно запрашивает данные, выполняет расчёты и возвращает отчёт.
    """
    # 1. Запрос имени (без валидации)
    user_name = input("Введите ваше имя: ")

    # 2. Ввод возраста с повторными попытками при ошибке
    while True:
        age_str = input("Сколько вам лет? ")
        try:
            # вызываем валидатор, который может выбросить исключение
            user_age = validate_positive_int(age_str)
            # если дошли до этой строки – ввод корректен
            print(f"Вы ввели возраст: {user_age} лет")
            break                     # выходим из цикла
        except ValueError as e:
            print(e)                  # сообщение об ошибке и повтор цикла

    # 3. Ввод веса (аналогично)
    while True:
        weight_str = input("Каков ваш вес (в кг)? ")
        try:
            user_weight = validate_positive_float(weight_str)
            print(f"Вы ввели значение веса: {user_weight} кг")
            break
        except ValueError as e:
            print(e)

    # 4. Ввод роста (аналогично)
    while True:
        height_str = input("Введите рост в метрах через точку: ")
        try:
            user_height = validate_positive_float(height_str)
            print(f"Вы ввели значение роста: {user_height} м")
            break
        except ValueError as e:
            print(e)

    # 5. Вычисления
    # Индекс массы тела (формула Кетле)
    bmi = round(user_weight / (user_height ** 2), 1)
    # Рекомендуемая норма воды: 30 мл на 1 кг веса, переводим в литры
    water_need_l = round(user_weight * 30 / 1000, 1)

    # 6. Формирование итоговой строки-отчёта с помощью f-строк
    return (
        f"\nПривет, {user_name}!"
        f"\nОтчет для пользователя:"
        f"\n{user_name} ({user_age} л.)"
        f"\nИндекс массы вашего тела: {bmi}"
        f"\nРекомендуемая норма воды: {water_need_l} л в день"
        f"\nРасчет окончен. Будьте здоровы!"
    )


# Точка входа: если файл запущен напрямую, а не импортирован как модуль,
# вызываем main() и печатаем результат
if __name__ == "__main__":
    print(main())

# Проект FitLife - MVP-версия 1.0
# Программа для расчёта индекса массы тела (ИМТ) и рекомендуемой нормы воды

import sys

# Настройка кодировки вывода для корректного отображения кириллицы в Windows
sys.stdout.reconfigure(encoding="utf-8")


def validate_positive_int(value):
    """
    Проверяет, что строка является целым положительным числом.
    Если проверка пройдена, возвращает число (int).
    Иначе выбрасывает ValueError с пояснением.
    """
    if value <= 0:
        raise ValueError("Число должно быть положительным")


def validate_positive_float(value):
    """
    Проверяет, что строка является положительным числом с плавающей точкой.
    Возвращает число (float) или выбрасывает ValueError.
    """
    if value <= 0:
        raise ValueError("Значение должно быть больше нуля")


def main():  # noqa: C901  # подавляем предупреждение о сложности
    """
    Основная функция программы.
    Последовательно запрашивает данные, выполняет расчёты и возвращает отчёт.
    """
    user_name = input("Введите ваше имя: ")
    while True:
        try:
            user_age = int(input("Сколько вам лет? "))
            validate_positive_int(user_age)
            print(f"Вы ввели возраст: {user_age} лет")
            break
        except ValueError as e:
            print(f"Ошибка: {e}")

    while True:
        try:
            user_weight = float(input("Каков ваш вес (в кг)? "))
            validate_positive_float(user_weight)
            print(f"Вы ввели значение веса: {user_weight} кг")
            break
        except ValueError as e:
            print(f"Ошибка: {e}")

    while True:
        try:
            user_height = float(input("Введите рост в метрах через точку: "))
            validate_positive_float(user_height)
            print(f"Вы ввели значение роста: {user_height} м")
            break
        except ValueError as e:
            print(f"Ошибка: {e}")

    #  Вычисления
    # Индекс массы тела (формула Кетле)
    bmi = round(user_weight / (user_height**2), 1)
    # Рекомендуемая норма воды: 30 мл на 1 кг веса, переводим в литры
    water_need_l = round(user_weight * 30 / 1000, 1)

    #  Формирование итоговой строки-отчета с помощью f-строк
    return f"""Привет, {user_name}!
Отчет для пользователя:
Индекс массы вашего тела: {bmi}
Рекомендуемая норма воды: {water_need_l} л в день
Расчет окончен. Будьте здоровы!"""


if __name__ == "__main__":
    print(main())

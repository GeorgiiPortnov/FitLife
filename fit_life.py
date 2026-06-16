# Проект FitLife - MVP версия 1.0

import sys
sys.stdout.reconfigure(encoding='utf-8')


def main():
    """Основная функция программы FitLife."""
    # 1. Знакомство
    # Запрашиваем у пользователя имя и сохраняем в переменную user_name
    user_name = input("Введите Ваше имя: ")
    # Запрашиваем возраст, сохраняем в user_age и преобразуем в число
    user_age = input("Сколько вам лет? ")
    age_int = int(user_age)
    # 2. Сбор данных
    # Запрашиваем вес (в кг) и сохраняем в user_weight (тип float)
    user_weight = input("Каков ваш вес (в кг)? ")
    weight_float = float(user_weight)
    while True:
        try:  # применяем try-except, чтобы избежать ошибок ввода
            user_height = input("Введите рост в метрах через точку: ")
            height_float = float(user_height.replace(',', '.'))  # replace
        # на случай, если пользователь ошибется и напечает запятую
            if height_float <= 0:
                print("Рост должен быть больше нуля. Попробуйте еще раз")
                continue
            break
        except ValueError:
            print("Некорректный ввод. Используйте цифры и точку!")
    # 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
    # Формула ИМТ: вес разделить на (рост в квадрате)
    bmi = round(weight_float / (height_float ** 2), 1)  # расчет индекса
    # массы тела
    # округляем результат до одного знака после запятой
    # Подсчет воды: вес * 30 мл
    # Расчет water_needed
    water_ml = weight_float * 30  # Расчет нужного числа воды
    water_l = round((water_ml / 1000), 1)  # Перевод объема воды в литры

    # 4. Вывод красивого результата
    # Используем f-строку, чтобы вывести приветствие
    result = (
        f"\nПривет, {user_name}!"
        f"\nОтчет для пользователя:"
        f"\n{user_name} ({age_int} л.)"
        f"\nИндекс массы вашего тела: {bmi}"
        f"\nРекомендуемая норма воды: {water_l} л в день"
        f"\nРасчет окончен. Будьте здоровы!"
    )
    print(f"{result}")  # для пользователя
    return result  # для тестов


if __name__ == "__main__":
    main()

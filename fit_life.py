# Проект FitLife - MVP версия 1.0
import sys

sys.stdout.reconfigure(encoding='utf-8')


def main():
    """Основная функция программы FitLife."""
    # 1. Знакомство
    user_name = input("Введите Ваше имя: ")
    while True:
        age_str = input("Сколько вам лет? ")
        try:
            user_age = int(age_str)
            if user_age <= 0:
                print("Число должно быть положительным")
                continue
            print(f"Вы ввели возраст: {user_age} лет")
            break
        except ValueError:
            print("Вы ввели не то число. Попробуйте еще раз!")

    # 2. Сбор данных
    while True:
        weight_str = input("Каков ваш вес (в кг)? ")
        try:
            user_weight = float(weight_str)
            if user_weight > 0:
                print(f"Вы ввели значение веса: {user_weight} кг")
                break
            else:
                print("Вес должен быть больше нуля!")
        except ValueError:
            print("Некорректный ввод. Используйте цифры больше нуля и точку!")

    while True:
        height_str = input("Введите рост в метрах через точку: ")
        try:
            user_height = float(height_str)
            if user_height > 0:
                print(f"Вы ввели значение роста: {user_height} м")
                break
            else:
                print("Рост должен быть больше нуля!")
        except ValueError:
            print("Некорректный ввод. Используйте цифры больше нуля и точку!")

    # 3. Логика расчётов
    bmi = round(user_weight / (user_height ** 2), 1)
    WATER_NEED_ML = user_weight * 30
    WATER_NEED_L = round(WATER_NEED_ML / 1000, 1)

    # 4. Формирование результата
    result = (
        f"\nПривет, {user_name}!"
        f"\nОтчет для пользователя:"
        f"\n{user_name} ({user_age} л.)"
        f"\nИндекс массы вашего тела: {bmi}"
        f"\nРекомендуемая норма воды: {WATER_NEED_L} л в день"
        f"\nРасчет окончен. Будьте здоровы!"
    )

    return result


if __name__ == "__main__":
    print(main())

# Проект FitLife - MVP версия 1.0
import sys
sys.stdout.reconfigure(encoding='utf-8')

def main():
   
    # 1. Знакомство
    user_name = input("Введите Ваше имя: ")
    user_age = input("Сколько вам лет? ")
    age_int = int(user_age)

    # 2. Сбор данных
    user_weight = input("Каков ваш вес (в кг)? ")
    weight_float = float(user_weight)

    while True:
        try:
            user_height = input("Введите рост в метрах через точку: ")
            height_float = float(user_height.replace(',', '.'))
            if height_float <= 0:
                print("Рост должен быть больше нуля. Попробуйте еще раз")
                continue
            break
        except ValueError:
            print("Некорректный ввод. Используйте цифры и точку!")

    # 3. Логика расчётов
    bmi = round(weight_float / (height_float ** 2), 1)
    water_ml = weight_float * 30
    water_l = round(water_ml / 1000, 1)

    # 4. Формирование результата
    result = (
        f"\nПривет, {user_name}!"
        f"\nОтчет для пользователя:"
        f"\n{user_name} ({age_int} л.)"
        f"\nИндекс массы вашего тела: {bmi}"
        f"\nРекомендуемая норма воды: {water_l} л в день"
        f"\nРасчет окончен. Будьте здоровы!"
    )

    print(f"{result}")
    return result


if __name__ == "__main__":
    main()

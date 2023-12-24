def calculate_fuel():
    while True:
        try:
            fraction = input("Дробь: ")
            x, y = fraction.split('/')
            x = int(x)
            y = int(y)

            if y == 0 or x > y:
                raise ValueError

            percentage = round(x / y * 100)

            if percentage <= 1:
                print('E')
            elif percentage >= 99:
                print('F')
            else:
                print(f'{percentage}%')

            break

        except ValueError:
            print('Неправильный формат дроби. Попробуйте снова.')
        except ZeroDivisionError:
            print('Знаменатель не может быть равен нулю. Попробуйте снова.')

calculate_fuel()